# This script parses output from test script.  It compares the answer with the student output.  If they are the same, the student result is deemed correct, and full credit is assigned.  If they are different, zero credit is assigned for the corresponding test, and the difference between the answer and the student result is recorded in the sql database.
#Ted Golfinopoulos, 7 July 2014

import re
import sys
import difflib
import sqlite3

#Get database holding student results for this day
conn=sqlite3.connect('day4results.db')
c=conn.cursor()

student_username = re.split("/",sys.argv[1])[-1]

buffer_size=4*5000 #Limit buffer size to 20000 bytes (5000-20000 characters, depending on encoding)
data_file=open("out.txt","r",buffer_size) #Open data file for reading.

total_points=0
total_points_possible=0
#Parse tests
test_num=0
missed_problems=[]
for test in re.findall("<test>([\s\S]*?)</test>",data_file.read()) :
    test_num+=1
    point_value=int(re.findall("<value>(\d+)</value>",test)[0])
    test_title=re.findall("<title>([\s\S]+?)</title>",test)[0]
    answer=re.findall("<answer>([\s\S]*?)</answer>",test)
    student_output=re.findall("<student>([\s\S]*?)</student>",test)
    diff_from_answer=""
    total_points_possible += point_value
    if(answer==student_output) :
        total_points += point_value
        score = point_value
    else :
        score=0
        missed_problems.append(test_num)
        diff_from_answer="".join([x for x in difflib.context_diff(answer,student_output)]) #Concatenate differences into one string
        temp=difflib.context_diff(answer,student_output)

    # Insert a row of data
    #Store results as tuple.  Data is (username text, title text, value real, score real, diff_from_answer text)
    student_data=(student_username, test_title, point_value, score, diff_from_answer)

    c.execute("INSERT INTO results VALUES (?,?,?,?,?)",student_data)

for row in c.execute('SELECT * FROM results ORDER BY score'):
    print row

print("Student Username: "+student_username)
print("Total points: "+str(total_points)+"/"+str(total_points_possible))
print("Which problem/s has/ve an issue: "+",".join([str(x) for x in missed_problems]))
data_file.close()
conn.close() #Close database

import sys
import re
import threading
import day4 as student
import day4answers as answers

#Run tests
time_limit=30.0 #Maximum number of seconds allowed for any student code test

student_username = re.split("/",sys.argv[1])[-1] #Get username from command line

print("<unit_test>")
### New test
print("<test><title>Test 1: Test border()</title><value>1</value>")
test_args=(8,)
print("<answer>") #Record correct answer first
answers.border(*test_args)
print("</answer>")
print("<student>") #Record student answer afterward
student.border(*test_args) 
print("</student>")
print("</test>")
### End test

### New test
print("<test><title>Test 2: Test print_with_border()</title><value>1</value>")
test_args=("hello world",3)
print("<answer>")
answers.print_with_border(*test_args) #Asterisk expands tuple input into all input parameters
print("</answer>")
print("<student>")
student.print_with_border(*test_args)
print("</student>")
print("</test>") 
### End test

### New test
test_args=("Hello world 3 spaces follow!   ",)
print("<test><title>Test 3: print_auto_border()</title><value>1</value>")
print("<answer>")
answers.print_auto_border(*test_args)
print("</answer>")
print("<student>")
student.print_auto_border(*test_args)
print("</student>")
print("</test>")
### End test

### New test
test_args=("",) #Empty string argument
print("<test><title>Test 4: print_auto_border()</title><value>1</value>")
print("<answer>")
answers.print_auto_border(*test_args)
print("</answer>")
print("<student>")
student.print_auto_border(*test_args)
print("</student>")
print("</test>")
### End test

### New test
test_args=(" ",) #
print("<test><title>Test 5: print_auto_border()</title><value>1</value>")
print("<answer>")
answers.print_auto_border(*test_args)
print("</answer>")
print("<student>")
student.print_auto_border(*test_args)
print("</student>")
print("</test>")
### End test

print("</unit_test>")

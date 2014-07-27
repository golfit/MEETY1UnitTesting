import sqlite3
conn=sqlite3.connect('day4results.db')

c=conn.cursor()

# Create table
c.execute('''CREATE TABLE results
             (username text, title text, value real, score real, diff_from_answer text)''')

# Save (commit) the changes
conn.commit()

conn.close()

#!/bin/bash
#This bash script passes to all student directories and runs the given unit test code.  It prints the results to an output file for each directory.  The idea is that all student code will appear in Dropbox folders labeled by the students' usernames.
#Ted Golfinopoulos, June/July 2014

username=$1

python /share/MEET/2014Summer/Y1/Module1_4Functions/test1_mod1_4_functions.py $username > out.txt

python /share/MEET/2014Summer/Y1/Module1_4Functions/test2_mod1_4_functions.py $username

#Remove output file.
#rm out.txt

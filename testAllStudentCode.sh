#!/bin/bash
#This bash script passes to all student directories and runs the given unit test code.  It prints the results to an output file for each directory.  The idea is that all student code will appear in Dropbox folders labeled by the students' usernames.
#Ted Golfinopoulos, June/July 2014

script_name=$1

#echo $script_name

code_parent_directory="/home/golfit/Dropbox/MEET/StudentCode"
cd "$code_parent_directory"

#-maxdepth option is to eliminate recursion in find call, in case there are subdirectories
for student_username in $(find . -type d -maxdepth 1)
do
    cd "$student_username"
    bash "$script_name" "$student_username"
    cd "$code_parent_directory"
done

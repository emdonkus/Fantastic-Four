#!/bin/bash
# Script:
#  retrieveURL.sh
#
# Purpose:
#   Test retrieveURL.sh
#
# Inputs:
#   $1 = Test Case
#   $2 = 1 for pausing after each test, else 0 
#
# Outputs:
#   Tested Results in test_case_results
#
# Notes:
#   
#
# Exits
#   0 = success
#   1 = bad url
#   2 = bad grep 
#   3 = missing file
#    
# Changelog:
#    Date (MM-DD-YYYY)     Name      Change Description
#    02-18-2024            EDonkus   Initial Creation
#
#------------------------------------------------------------------
#------------------------------------------------------------------

#------------
# reportSuccess : reports the success of a test case and assigns string to 
#      the test_case_results array
# Inputs:
#    test_case=$1
#    status=$2
#    expected_status=$3
#------------


echo  "Changing to correct Directory: /home/jovyan/3308class/Fantastic-Four"

cd /home/jovyan/3308class/Fantastic-Four

echo "Creating Test Case Results"
NUM_TESTCASE=3
declare -a test_case_results
for (( i=0; i<=$NUM_TESTCASE; i++ ))
do 
    test_case_results[$case]=" "
    echo ${test_case_results[$case]}
done

if [[ $1 -eq 1 || "$1" == "ALL" ]];
then
    echo "_________________________________________________"
    echo "----------------CASE 1: Bad url----------------"
    echo "_________________________________________________"
    test_case=1
    echo "Testing: extract_scripts.sh https://www.skinnytast.com/chicken-floretine/"
    extract_scripts/retrieveURL.sh https://www.skinnytast.com/chicken-floretine/
    
    status=$?
    expected_status=1
    echo "Error Status: $status"
    echo "Expected : $expected_status"
    if [[ $status -eq $expected_status ]];
    then
        test_case_results[$test_case] =  "CASE $test_case Successful"
        #status1="CASE 1 Successful"
    else
        test_case_results[$test_case] =  "CASE $test_case Unsuccessful"
        #status1="CASE 1 Unsuccesful"       
    fi
    
    if [[ $2 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
if [[ $1 -eq 1 || "$1" == "ALL" ]];
then
    echo "_________________________________________________"
    echo "----------------CASE 2: Not recipe URL----------------"
    echo "_________________________________________________"
    test_case=2    
    test_url="https://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used"
    echo "Testing: extract_scripts.sh $test_url"
    extract_scripts/retrieveURL.sh $test_url
    
    status=$?
    expected_result=1
    echo "Error Status: $status"
    echo "Expected : $expected_status"
    if [[ $status -eq $expected_status ]];
    then
        test_case_results[$test_case] =  "CASE $test_case Successful"
        #status1="CASE 1 Successful"
    else
        test_case_results[$test_case] =  "CASE $test_case Unsuccessful"
        #status1="CASE 1 Unsuccesful"       
    fi
    
    if [[ $2 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
if [[ $1 -eq 3 || "$1" == "ALL" ]];
then
    echo "_________________________________________________"
    echo "----------------CASE 3: Good URL----------------"
    echo "_________________________________________________"
    test_case=3    
    test_url="https://www.skinnytaste.com/chicken-florentine/"
    echo "Testing: extract_scripts.sh $test_url"
    extract_scripts/retrieveURL.sh $test_url
    
    status=$?
    expected_result=0
    echo "Error Status: $status"
    echo "Expected : $expected_status"
    if [[ $status -eq $expected_status ]];
    then
        test_case_results[$test_case] =  "CASE $test_case Successful"
        #status1="CASE 1 Successful"
    else
        test_case_results[$test_case] =  "CASE $test_case Unsuccessful"
        #status1="CASE 1 Unsuccesful"       
    fi
    
    if [[ $2 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
echo "_________________________________________________"
echo "--------------------Summary-----------------------------------"
echo "_________________________________________________"
counter=1
for i in ${test_case_results[@]}
do
    echo -e "CASE $counter: $i \n"
    counter=counter+1
done
read -p "Press [ENTER] to continue"

echo "--------------------Cleaning Up------------------------------"
read -p "Press [ENTER] to clean up directory"
 
pwd
rm -rf Recipes/*
read -p "Press [ENTER] to End"
clear
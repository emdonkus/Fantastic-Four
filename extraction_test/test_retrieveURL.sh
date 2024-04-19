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
#    03-07-2024            EDonkus   Added webpages with different HTML formatting 
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

if [[ -z $1 ]];
then
    echo -e "No Input.\n"
    echo -e "USAGE: $0 [Test Case Number |'ALL'] [1 for pauses | 0 for running through]\n"
    echo "NOTE: Script will always pause after summary and in cleanup"
    echo "NOTE: -1 for manul url and manul checking"
    exit -1
fi
currentDir=${pwd}
echo  "Changing to correct Directory: /home/jovyan/3308class/Fantastic-Four"

cd /home/jovyan/3308class/Fantastic-Four

echo "Creating Test Case Results"
#------------
# UPDATE THIS FOR NEW TEST CASES
#-------------
NUM_TESTCASE=9
declare -a test_case_results
test_case_results[0]="$NUM_TESTCASE Test Cases"
for (( i=1; i<=$NUM_TESTCASE; i++ ))
do 
    test_case_results[$i]="CASE $i Not Run"
    echo ${test_case_results[$i]}
done

#------------
# UPDATE THIS FOR NEW TEST CASES
#-------------
if [[ $1 -eq 1 || "$1" == "ALL" ]];
then
    echo "_________________________________________________"
    echo "----------------CASE 1: Bad url----------------"
    echo "_________________________________________________"
    #-------------------
    # UPDATE CASE NUM and URL FOR NEW TEST CASES
    #-------------------
    test_case=1
    echo "Testing: extract_scripts.sh https://www.skinnytast.com/chicken-floretine/"
    extract_scripts/retrieveURL.sh https://www.skinnytast.com/chicken-floretine/
    
    status=$?
    #-------------------
    # UPDATE THIS FOR NEW TEST CASES
    #-------------------
    expected_status=1
    echo "Error Status: $status"
    echo "Expected : $expected_result"
    if [[ $status -eq $expected_result ]];
    then
        test_case_results[$test_case]="CASE $test_case Successful"
        #status1="CASE 1 Successful"
    else
        test_case_results[$test_case]="CASE $test_case Unsuccessful"
        #status1="CASE 1 Unsuccesful"       
    fi
    
    if [[ $2 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
#------------
# UPDATE THIS FOR NEW TEST CASES
#-------------
if [[ $1 -eq 1 || "$1" == "ALL" ]];
then
    echo "_________________________________________________"
    echo "----------------CASE 2: Not recipe URL----------------"
    echo "_________________________________________________"
    #-------------------
    # UPDATE CASE NUM and URL FOR NEW TEST CASES
    #-------------------
    test_case=2    
    test_url="https://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used"
    echo "Testing: extract_scripts.sh $test_url"
    extract_scripts/retrieveURL.sh $test_url
    
    status=$?
    #-------------------
    # UPDATE THIS FOR NEW TEST CASES
    #-------------------
    expected_result=1
    echo "Error Status: $status"
    echo "Expected : $expected_result"
    if [[ $status -eq $expected_result ]];
    then
        test_case_results[$test_case]="CASE $test_case Successful"
        #status1="CASE 1 Successful"
    else
        test_case_results[$test_case]="CASE $test_case Unsuccessful"
        #status1="CASE 1 Unsuccesful"       
    fi
    
    if [[ $2 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
#------------
# UPDATE THIS FOR NEW TEST CASES
#-------------
if [[ $1 -eq 3 || "$1" == "ALL" ]];
then
    echo "_________________________________________________"
    echo "----------------CASE 3: Good URL----------------"
    echo "_________________________________________________"
    #-------------------
    # UPDATE CASE NUM and URL FOR NEW TEST CASES
    #-------------------
    test_case=3    
    test_url="https://www.skinnytaste.com/chicken-florentine/"
    echo "Testing: extract_scripts.sh $test_url"
    extract_scripts/retrieveURL.sh $test_url
    
    status=$?
    #-------------------
    # UPDATE THIS FOR NEW TEST CASES
    #-------------------
    expected_result=0
    echo "Error Status: $status"
    echo "Expected : $expected_result"
    if [[ $status -eq $expected_result ]];
    then
        test_case_results[$test_case]="CASE $test_case Successful"
        #status1="CASE 1 Successful"
    else
        test_case_results[$test_case]="CASE $test_case Unsuccessful"
        #status1="CASE 1 Unsuccesful"       
    fi
    
    if [[ $2 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
#------------
# UPDATE THIS FOR NEW TEST CASES
#-------------
if [[ $1 -eq 4 || "$1" == "ALL" ]];
then
    echo "_________________________________________________"
    echo "----------------CASE 4: Missing Instruction.txt----------------"
    echo "_________________________________________________"
    #-------------------
    # UPDATE CASE NUM and URL FOR NEW TEST CASES
    #-------------------
    test_case=4    
    test_url="https://www.budgetbytes.com/cranberry-apple-baked-oatmeal/"
    echo "Testing: extract_scripts.sh $test_url"
    extract_scripts/retrieveURL.sh $test_url
    
    status=$?
    #-------------------
    # UPDATE THIS FOR NEW TEST CASES
    #-------------------
    expected_result=0
    echo "Error Status: $status"
    echo "Expected : $expected_result"
    if [[ $status -eq $expected_result ]];
    then
        test_case_results[$test_case]="CASE $test_case Successful"
        filepath='Recipes/budgetbytes/Apple_Cranberry_Baked_Oatmeal/Apple_Cranberry_Baked_Oatmeal_instructions.txt'
        if [[  ! -s $filepath ]];
        then
            test_case_results[$test_case]="CASE $test_case Unsuccessful"
        fi
        #status1="CASE 1 Successful"
    else
        test_case_results[$test_case]="CASE $test_case Unsuccessful"
        #status1="CASE 1 Unsuccesful"       
    fi
    
    if [[ $2 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
#------------
# UPDATE THIS FOR NEW TEST CASES
#-------------
if [[ $1 -eq 5 || "$1" == "ALL" ]];
then
    echo "_________________________________________________"
    echo "----------------CASE 5: No Input----------------"
    echo "_________________________________________________"
    #-------------------
    # UPDATE CASE NUM and URL FOR NEW TEST CASES
    #-------------------
    test_case=5    
    #test_url="https://www.budgetbytes.com/creamy-garlic-chicken/"
    echo "Testing: extract_scripts.sh "
    extract_scripts/retrieveURL.sh 
    
    status=$?
    #-------------------
    # UPDATE THIS FOR NEW TEST CASES
    #-------------------
    expected_result=5
    echo "Error Status: $status"
    echo "Expected : $expected_result"
    if [[ $status -eq $expected_result ]];
    then
        test_case_results[$test_case]="CASE $test_case Successful"
        #status1="CASE 1 Successful
    else
        test_case_results[$test_case]="CASE $test_case Unsuccessful"
        #status1="CASE 1 Unsuccesful"       
    fi
    
    if [[ $2 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
#------------
# UPDATE THIS FOR NEW TEST CASES
#-------------
if [[ $1 -eq 6 || "$1" == "ALL" ]];
then
    echo "_________________________________________________"
    echo "----------------CASE 6: Missing Instruction.txt 2----------------"
    echo "_________________________________________________"
    #-------------------
    # UPDATE CASE NUM and URL FOR NEW TEST CASES
    #-------------------
    test_case=6     
    test_url="https://www.budgetbytes.com/creamy-garlic-chicken/"
    echo "Testing: extract_scripts.sh $test_url"
    extract_scripts/retrieveURL.sh $test_url
    
    status=$?
    #-------------------
    # UPDATE THIS FOR NEW TEST CASES
    #-------------------
    expected_result=0
    echo "Error Status: $status"
    echo "Expected : $expected_result"
    if [[ $status -eq $expected_result ]];
    then
        test_case_results[$test_case]="CASE $test_case Successful"
        filepath='Recipes/budgetbytes/Creamy_Garlic_Chicken/Creamy_Garlic_Chicken_instructions.txt'
        if [[  ! -s $filepath ]];
        then
            test_case_results[$test_case]="CASE $test_case Unsuccessful"
        fi
        #status1="CASE 1 Successful"
    else
        test_case_results[$test_case]="CASE $test_case Unsuccessful"
        #status1="CASE 1 Unsuccesful"       
    fi
    
    if [[ $2 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
#------------
# UPDATE THIS FOR NEW TEST CASES
#-------------
if [[ $1 -eq 7 || "$1" == "ALL" ]];
then
    echo "_________________________________________________"
    echo "----------------CASE 7: Not a www.----------------"
    echo "_________________________________________________"
    #-------------------
    # UPDATE CASE NUM and URL FOR NEW TEST CASES
    #-------------------
    test_case=7     
    test_url="https://moonandspoonandyum.com/slow-cooker-roasted-potatoes/?utm_source=msn&utm_medium=page&utm_campaign=msn#recipe"
    echo "Testing: extract_scripts.sh $test_url"
    extract_scripts/retrieveURL.sh $test_url
    
    status=$?
    #-------------------
    # UPDATE THIS FOR NEW TEST CASES
    #-------------------
    expected_result=0
    echo "Error Status: $status"
    echo "Expected : $expected_result"
    if [[ $status -eq $expected_result ]];
    then
        test_case_results[$test_case]="CASE $test_case Successful"
        filepath='Recipes/moonandspoonandyum/Easy_Slow_Cooker_Roasted_Potatoes/Easy_Slow_Cooker_Roasted_Potatoes_instructions.txt'
        if [[  ! -s $filepath ]];
        then
            test_case_results[$test_case]="CASE $test_case Unsuccessful"
        fi
        #status1="CASE 1 Successful"
    else
        test_case_results[$test_case]="CASE $test_case Unsuccessful"
        #status1="CASE 1 Unsuccesful"       
    fi
    
    if [[ $2 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
#------------
# UPDATE THIS FOR NEW TEST CASES
#-------------
if [[ $1 -eq 8 || "$1" == "ALL" ]];
then
    echo "_________________________________________________"
    echo "----------------CASE 8: Multiple href pages----------------"
    echo "_________________________________________________"
    #-------------------
    # UPDATE CASE NUM and URL FOR NEW TEST CASES
    #-------------------
    test_case=8    
    test_url="https://www.halfbakedharvest.com/one-pot-chili-mac-and-cheese/"
    echo "Testing: extract_scripts.sh $test_url"
    extract_scripts/retrieveURL.sh $test_url
    
    status=$?
    #-------------------
    # UPDATE THIS FOR NEW TEST CASES
    #-------------------
    expected_result=0
    echo "Error Status: $status"
    echo "Expected : $expected_result"
    if [[ $status -eq $expected_result ]];
    then
        test_case_results[$test_case]="CASE $test_case Successful"
        filepath='Recipes/halfbakedharvest/One_Pot_Chili_Mac_and_Cheese./One_Pot_Chili_Mac_and_Cheese._instructions.html'
        if [[  ! -s $filepath ]];
        then
            test_case_results[$test_case]="CASE $test_case Unsuccessful"
        fi
        #status1="CASE 1 Successful"
    else
        test_case_results[$test_case]="CASE $test_case Unsuccessful"
        #status1="CASE 1 Unsuccesful"       
    fi
    
    if [[ $2 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
#------------
# UPDATE THIS FOR NEW TEST CASES
#-------------
if [[ $1 -eq 9 || "$1" == "ALL" ]];
then
    echo "_________________________________________________"
    echo "----------------CASE 9: Multiple tag in instruction html----------------"
    echo "_________________________________________________"
    #-------------------
    # UPDATE CASE NUM and URL FOR NEW TEST CASES
    #-------------------
    test_case=9   
    test_url="https://damndelicious.net/2022/10/14/perfect-pot-roast/ "
    echo "Testing: extract_scripts.sh $test_url"
    extract_scripts/retrieveURL.sh $test_url
    
    status=$?
    #-------------------
    # UPDATE THIS FOR NEW TEST CASES
    #-------------------
    expected_result=0
    echo "Error Status: $status"
    echo "Expected : $expected_result"
    if [[ $status -eq $expected_result ]];
    then
        test_case_results[$test_case]="CASE $test_case Successful"
        filepath='Recipes/damndelicious/Perfect_Pot_Roast/Perfect_Pot_Roast_instructions.txt'
        if [[  ! -s $filepath ]];
        then
            test_case_results[$test_case]="CASE $test_case Unsuccessful"
        fi
        #status1="CASE 1 Successful"
    else
        test_case_results[$test_case]="CASE $test_case Unsuccessful"
        #status1="CASE 1 Unsuccesful"       
    fi
    
    if [[ $2 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
#------------
# UPDATE THIS FOR NEW TEST CASES
#-------------
if [[ $1 -eq -1 ]];
then
    echo "_________________________________________________"
    echo "----------------CASE Manual: Entering a URL----------------"
    echo "_________________________________________________"
    #-------------------
    # UPDATE CASE NUM and URL FOR NEW TEST CASES
    #-------------------
    test_case=""     
    read -p "Please enter a website: " test_url
    echo $test_url
    
    echo "Testing: extract_scripts.sh $test_url"
    extract_scripts/retrieveURL.sh $test_url
    
    #NO Auto VALIDATION ON this ONE Manual
    ls -lR Recipes/
    find Recipes/ -iname "*_*.txt" | xargs cat
    
    if [[ $2 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue to cleanup"
    fi
fi
if [[ $1 -ne -1 ]]; 
then
    echo "_________________________________________________"
    echo "--------------------Summary-----------------------------------"
    echo "_________________________________________________"

    for (( i=0; i<=$NUM_TESTCASE ; i=i+1 ));
    do
        echo "${test_case_results[$i]}"
    done
    read -p "Press [ENTER] to continue"
fi
echo "--------------------Cleaning Up------------------------------"
read -p "Press [ENTER] to clean up directory"
 
pwd
rm -rf Recipes/*
cd $currentDir
read -p "Press [ENTER] to End"
clear
exit
#https://www.skinnytaste.com/shrimp-stir-fry/
#https://www.recipetineats.com/spicy-asian-cucumber-salad/
#https://www.recipetineats.com/vietnamese-caramelised-pork-bowls/
#https://moonandspoonandyum.com/slow-cooker-roasted-potatoes/?utm_source=msn&utm_medium=page&utm_campaign=msn#recipe
#https://www.justonecookbook.com/ginger-tea/
#https://www.justonecookbook.com/nama-donuts/
#https://www.justonecookbook.com/vegetarian-udon/
#https://www.halfbakedharvest.com/one-pot-chili-mac-and-cheese/
#https://damndelicious.net/2022/10/14/perfect-pot-roast/


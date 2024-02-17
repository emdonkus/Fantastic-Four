#!/bin/bash -x
# Script:
#  extractInstructions.sh
#
# Purpose:
#   extract the instructions from recipe
#
# Inputs:
#   Recipe print URL
#
# Outputs:
#   extracted text file
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
#    02-16-2024            EDonkus   Initial Creation
#
#------------------------------------------------------------------
#------------------------------------------------------------------
DEBUG=1
#---------------
# Only echoes if debug is turned on
#---------------
decho () {
    if [[ $DEBUG == 1 ]];
    then
        echo $1
        echo ""
    fi
}

#-------------
# Reassign input
#-------------
recipeFile=$1
# example: skinnytaste/Chicken_Florentine/Chicken_Florentine_recipe.html
if [[ ! -e $recipeFile ]];
then
    decho "Cannot find $recipeFile"
    exit 3
fi
#----------------
# Trim the recipe part off and create path to instrcution html and the path for txt
#----------------
tempHTML="${recipeFile%_recipe.html}"
decho $tempHTML
instructionHTML="${tempHTML}_instructions.html"
instructionTXT="${tempHTML}_instructions.txt"

#-----------------
# Grep out the instruction html from recipe print and put into instructionhtml
#-----------------
grep -oE "<ul.*recipe-instructions.*<\/ul>" $recipeFile > $instructionHTML


# Not Sure what I need this for now, but gonna keep it just in case
if [[ 0 == 1 ]];
then
    filePath="${recipeFile%/*}"
    decho $filePath
fi


#-----------------
# Process instructions.html and return atext file of instructions
#-----------------
python3 extract_scripts/dataParser.py $instructionHTML

echo "Extracion Complete"
exit 0
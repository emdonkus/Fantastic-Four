#!/bin/bash
# Script:
#  extractIngredients.sh
#
# Purpose:
#   extract the ingredietns from recipe
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
#    02-25-2024            EDonkus   Initial Creation
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
decho "==============Starting $0 ============="
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
ingredientsHTML="${tempHTML}_ingredients.html"
ingredientsTXT="${tempHTML}_ingredients.txt"

#-----------------
# Grep out the instruction html from recipe print and put into instructionhtml
#-----------------
grep -oE "<ul.*recipe-ingredient.*>.*<\/ul>" $recipeFile > $ingredientsHTML


# Not Sure what I need this for now, but gonna keep it just in case
if [[ 0 == 1 ]];
then
    filePath="${recipeFile%/*}"
    decho $filePath
fi


#-----------------
# Process instructions.html and return atext file of instructions
#-----------------
python3 -m extract_scripts.dataParser $ingredientsHTML 2

echo "Extracion Complete"
exit 0
#!/bin/bash -x
# Script:
#  extratctImage.sh
#
# Purpose:
#   Retrieves the image file from Recipe HTML
#
# Inputs:
#   REcipe HTML file path
#
# Outputs:
#   extracted image file
#
# Notes:
#   
#
# Exits
#   0 = success
#   1 = bad url
#   2 = bad grep 
#   3 = missing file
#   4 = missing script
#   5 = no input
#    
# Changelog:
#    Date (MM-DD-YYYY)     Name      Change Description
#    03-10-2024            EDonkus   Initial Creation

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
imageFile="${tempHTML}_image.jpg"

#-----------------
# Grep out the image tag from recipe print
#-----------------
imageGrep=$(grep -Ei recipe-image $recipeFile | grep -Eo 'src=.*wp-content.*\.(jpg|png)\"')
decho $imageGrep

if [[ ! $imageGrep ]];
then
    exit 2
fi
#-----------------
# Remove the beginning src=" and the end "
#-----------------
srcRemoved=${imageGrep#'src="'}
decho $srcRemoved

imageHTML=${srcRemoved%'"'}
decho $imageHTML

#-----------------
# Wget the image and save to file
#-----------------
wget --output-document=$imageFile $imageHTML

status=$?
if [[ $status -ne 0 ]];
then
    exit $status
else
    exit 0
fi
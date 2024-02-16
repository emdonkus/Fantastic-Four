#!/bin/bash
# Script:
#  retrieveURL.sh
#
# Purpose:
#   Validates and retireve the URL and puts it into a html file within directory
#
# Inputs:
#   Initial URL
#
# Outputs:
#   extracted html file
#
# Notes:
#   using h1 markers to find recipe title
#
# Exits
#   0 = success
#   1 = bad url
#   2 = bad grep 
#   3 = missing file
#    
# Changelog:
#    Date (MM-DD-YYYY)     Name      Change Description
#    02-15-2024            EDonkus   Initial Creation
#
#------------------------------------------------------------------
#------------------------------------------------------------------
DEBUG=1
# Only echoes if debug is turned on
decho () {
    if [[ $DEBUG == 1 ]];
    then
        echo $1
        echo ""
    fi
}


validateURL () {
    decho "Validating $1"
    
    local inputURL=$1
    
    #------------------
    # Valid Flag
    # --spider puts wget into a check mode rather download
    # -q = silent mode
    # Returns 0 if successful,  not 0 else
    #------------------
    local invalidurl_flag=$(wget --spider -q $inputURL)

    #------------------
    # If the weblink is good download to temp file
    #------------------
    if [[ $invalidurl_flag ]];
    then
        decho "ERROR: Bad URL"
        return 1
    fi
    
    return 0
}

#---------------
#---------------
# Extracts the name of the recipe from temp.html
#---------------
#---------------
extractRecipeName () {
    decho "Extracting Recipe Name"
    #---------------
    # Now that this is a function should check file exists before trying anything
    #---------------
    if [[ ! -e temp.html ]];
    then
        decho "ERROR: missing temp.html from extract"
        exit 3
    fi
    
    #---------------
    # Grep for the Recipe Title
    #---------------
    local grepTitle=$(grep -Eo '<h1.*\/h1>*' temp.html | grep -Eo '>.*<\/h1')

    #---------------
    # if grep can't find h1 markers, then we exit with bad staus
    #---------------
    if [[ ! $grepTitle ]];
    then
        decho "Couldn't find header"
        exit 2
    fi

    #--------------
    # Remove characters surrounding title and replace spaces with '_'
    #--------------

    decho $grepTitle

    #Finds and removes '>' from previous grep
    local tempTitle="${grepTitle/>/}"
    decho "TEMP Title: $tempTitle"

    # Finds and removes '</h1' from previous grep
    local tempTitle2="${tempTitle/<\/h1/}"
    decho "TEMP2 title: $tempTitle2"

    # Replaces spaces with '_'
    finalTitle="${tempTitle2// /\_}"
    decho "Final: $finalTitle"
    
}

#-------------------
# Get the wbesite name from input URL
#-------------------
extractWebsiteName () {
    local inputurl=$1
    #-----------------
    # Get just the name of website xyz in www.xyz.com
    #-----------------
    decho "Input: $inputurl"
    local tempURL="${inputurl#*www.}"
    decho "Shortened: $tempURL"

    # Since we stripped all leading characters before base name
    # We should be able to get the basenaem up to .com ending piece
    websiteName="${tempURL%.*}"

}

#-----------------
# Move temp.html to finalTitle.html, and under appropiate hierarchy structure
#-----------------
moveRawHTML () {
    #-----------------
    # Move temp.html to finalTitle.html, and under appropiate hierarchy structure
    #-----------------
    rawHTML="$websiteName/$finalTitle/${finalTitle}_raw.html"
    decho "RAWHTML: $rawHTML"

    decho "Moving raw HTML to subdir $websiteName/$finalTitle/"

    #VVVV---STUB---VVVV#
    mkdir -p $websiteName/$finalTitle/
    #^^^^---STUB---^^^^#

    mv temp.html $rawHTML

    recipeHTML="${finalTitle}_recipe.html"

}

#------------------
# extracts the print URL from print button HTML
#--------------------
extractWPRM_PrintURL () {

    decho "Retreiving print Directory from website"

    #------------------
    # wprm_print = WordPress Recipe Maker
    # Looks to be a fairly common plugin 
    #--------------------
    local grep_print_url=$(grep -ia "wprm_print" $rawHTML | grep -Eo 'href=\"https?:\/\/[^"]+\"'| grep -Eo '\"https?:\/\/[^"]+\"')
    echo "grepout: $grep_print_url"
    
    if [[ ! $grep_print_url ]];
    then
        decho "Couldn't find print url"
        exit 2
    fi

    #Trims leading quote
    local temp="${grep_print_url%\"}"
    decho "TEMP: $temp"

    #Trims trailing quote
    recipeurl="${temp#\"}"
    decho "RecipeURL: $recipeurl"
}
#==============================================================================
# MAIN SCRIPT
#==============================================================================
#-------------------
# Take input and give name
#-------------------
decho "Reassigning input"
inputurl=$1

validateURL $inputurl
status=$?
#-------------------
# If valid url, get the html file
#-------------------
if [[ $status -eq 0 ]];
then
    wget -q -O temp.html $inputurl
else
    exit $status
fi

#-------------------
# extracts recipe name from a header block
#-------------------
extractRecipeName
decho $finalTitle

#-------------------
# Get the wbesite name from input URL
#-------------------
extractWebsiteName $inputurl

#-----------------
# Move temp.html to finalTitle.html, and under appropiate hierarchy structure
#-----------------
moveRawHTML
#-----------------
# Verify that file does not exist in heirarchy
#-----------------
#Hallee:heirarchy
    #ingredients based off print page
#------------------
# extracts the print URL from print button HTML
#--------------------
extractWPRM_PrintURL

#------------------
# Validate print url. Should be good if grep worked
#------------------
validateURL $recipeurl
status=$?
#------------------
# If the weblink is good download to temp file
#------------------
if [[ $status -eq 0 ]];
then
    recipePath="$websiteName/$finalTitle/$recipeHTML"
    decho "Getting the recipe print page"
    wget -q -O $recipePath $recipeurl
fi

decho "Extraction Complete"
exit 0
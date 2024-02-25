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
#   4 = missing script
#    
# Changelog:
#    Date (MM-DD-YYYY)     Name      Change Description
#    02-15-2024            EDonkus   Initial Creation
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

#---------------
#---------------
# Validates a URL
#---------------
#---------------
validateURL () {
    decho "Validating $1"
    
    local inputURL=$1
    
    #------------------
    # Valid Flag
    # --spider puts wget into a check mode rather download
    # -q = silent mode
    # Returns 0 if successful,  not 0 else
    #------------------
    #local invalidurl_flag=$(wget --spider -q $inputURL)

    #------------------
    # If the weblink is good download to temp file
    #------------------
    if wget -q --spider $url 2>/dev/null;
    then
        decho "ERROR: Bad URL"
        exit 1
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
    recipePath="Recipes/$websiteName/$finalTitle/"
    rawHTML="$recipePath/${finalTitle}_raw.html"
    decho "RAWHTML: $rawHTML"

    # Validate existence of command else exit
    decho "Validating Directory"
    extract_valid=$( command -v extract_scripts/verifyHeirarchy.sh )
    if [ "$extract_valid" == "" ];
    then
        echo "Could Not find extract_scripts/verifyHeirarchy.sh"
        exit 4
    fi
    
    extract_scripts/verifyHeirarchy.sh $recipePath
    
    decho "Moving raw HTML to subdir Recipes/$websiteName/$finalTitle/"
    
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
#-------------------
# Checks value of given status
#-------------------
statusCheck () {
    status=$1
    if [[ $status -ne 0 ]];
    then
        exit $status
    fi
}
#==============================================================================
# MAIN SCRIPT
#==============================================================================
decho "==============Starting $0 ============="
#-------------------
# Take input and give name
#-------------------
decho "Reassigning input"
inputurl=$1
exitTest
validateURL $inputurl

#-------------------
# If valid url, get the html file
#-------------------
statusCheck $?
wget -q -O temp.html $inputurl

#-------------------
# extracts recipe name from a header block
#-------------------
extractRecipeName
statusCheck $?

decho $finalTitle

#-------------------
# Get the wbesite name from input URL
#-------------------
extractWebsiteName $inputurl
statusCheck $?
#-----------------
# Move temp.html to finalTitle.html, and under appropiate hierarchy structure
#-----------------
moveRawHTML
statusCheck $?

#Hallee:heirarchy
    #ingredients based off print page
#------------------
# extracts the print URL from print button HTML
#--------------------
extractWPRM_PrintURL
statusCheck $?

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
    recipePath="Recipes/$websiteName/$finalTitle/$recipeHTML"
    decho "Getting the recipe print page"
    wget -q -O $recipePath $recipeurl
fi

#-----------------
# Verify that file does not exist in heirarchy
#-----------------

decho "Extraction Complete. File at $recipePath"

#------------------
# call Dataparser if found
#------------------
decho "Running instruction script"

if [[ ! -e extract_scripts/dataParser.py ]];
then
    echo "Could Not find dataParser.py"
    exit 4
fi

exec ./extract_scripts/extractInstructions.sh $recipePath
decho "Extraction Complete"
exit 0
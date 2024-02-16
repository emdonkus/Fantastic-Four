#!/bin/sh
# Script:
#  retrieveURL.sh
#
# Purpose:
#  Validates and retireve the URL and puts it into a html file within directory
#
# Inputs:
#  Initial URL
#
# Outputs:
#  extracted html file
#
# Changelog:
#    Date (MM-DD-YYYY)     Name      Change Description
#    02-15-2024            EDonkus   Initial Creation
#
#------------------------------------------------------------------
#------------------------------------------------------------------

#-------------------
# Take input and give name
#-------------------
inputurl=$1

#------------------
# Valid Flag
# --spider puts wget into a check mode rather download
#------------------
validurl_flag=$(wget --spider -q $inputurl)

#------------------
# If the weblink is good download to temp file
if [[ ! $validurl_flag ]];
then
    wget -q -O temp.html $inputurl
else
    echo "Bad URL"
    exit 1
fi

#---------------
# Grep for the Recipe Title
#---------------
grepTitle=$(grep -iaE '<h1.*\/h1>*' temp.html | grep -Eo '>.*<\/h1')

#--------------
# Remove characters surrounding title and replace spaces with '_'
#--------------
echo $grepTitle
tempTitle="${grepTitle/>/}"
echo $tempTitle
tempTitle2="${tempTitle/<\/h1/}"
echo $tempTitle2
finalTitle="${tempTitle2/ /\_}"
echo $finalTitle

#-----------------
# Get just the name of website xyz in www.xyz.com
#-----------------
echo $inputurl
tempURL="${inputurl#*www.}"
echo $tempURL
if [[ $url1 == *".com"* ]];
then 
    websiteName="${tempURL%*.com*}"
    echo $websiteName
fi

#-----------------
# Verify that file does not exist in heirarchy
#-----------------


#-----------------
# Move temp.html to finalTitle.html, and under appropiate hierarchy structure
#-----------------
rawHTML="${finalTitle}_raw.html"
echo "Moving raw HTML to subdir"
mv temp.html $websiteName/$finalTitle/$rawHTML

recipeHTML="${finalTitle}_recipe.html"
echo "Retreiving print Direcotry from website"
grepout=$(grep -ia "print" SkinnyTasteR.html | grep -Eo 'href=\"https?:\/\/[^"]+\"'| grep -Eo '\"https?:\/\/[^"]+\"')
temp="${grepout%\"}"
echo $temp
recipeurl="${temp#\"}"
echo $recipeurl
wget -O $recipeHTML $recipeurl


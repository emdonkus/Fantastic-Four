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
fi

#---------------
# Grep for the Recipe Title
#---------------
grepTitle=$(grep -iaE '\"entry-title\">*' temp.html | grep -Eo '>.*<\/h1')

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
# Verify that file does not exist in heirarchy
#-----------------

#-----------------
# Move temp.html to finalTitle.html, and under appropiate hierarchy structure
#-----------------
mv temp.html $finalTitle.html


#wget -O SkinnyTasteR.html https://www.skinnytaste.com/white-chicken-chili/
#grepout=$(grep -ia "print" SkinnyTasteR.html | grep -Eo 'href=\"https?:\/\/[^"]+\"'| grep -Eo '\"https?:\/\/[^"]+\"')
#temp="${grepout%\"}"
#echo $temp
#recipeurl="${temp#\"}"
#echo $recipeurl
#wget -O SkinnyRecipeFinal.html $recipeurl
wget -O SkinnyTasteR.html https://www.skinnytaste.com/white-chicken-chili/
grepout=$(grep -ia "print" SkinnyTasteR.html | grep -Eo 'href=\"https?:\/\/[^"]+\"'| grep -Eo '\"https?:\/\/[^"]+\"')
temp="${grepout%\"}"
echo $temp
recipeurl="${temp#\"}"
echo $recipeurl
wget -O SkinnyRecipeFinal.html $recipeurl
./extract1.sh https://www.skinnytaste.com/chicken-florentine/
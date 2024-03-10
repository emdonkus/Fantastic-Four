#!/bin/bash
# Script:
#  genRecipes.sh
#
# Purpose:
#   Generates the Recipe directory for listed recipes here
#
# Inputs:
#   Add urls to URLs array
#
# Outputs:
#   Recipe files
#
# Notes:
#   
#
# Exits
#   0 = success
#   1 = error
#    
# Changelog:
#    Date (MM-DD-YYYY)     Name      Change Description
#    03-07-2024            EDonkus   Initial Creation
#
#------------------------------------------------------------------
#------------------------------------------------------------------

#------------
# URL that worked
#------------
URLs=(
    'https://www.skinnytaste.com/shrimp-stir-fry/'
    'https://moonandspoonandyum.com/slow-cooker-roasted-potatoes/?utm_source=msn&utm_medium=page&utm_campaign=msn#recipe'
    'https://www.skinnytaste.com/chicken-florentine/'
    'https://www.halfbakedharvest.com/one-pot-chili-mac-and-cheese/'
    'https://damndelicious.net/2022/10/14/perfect-pot-roast/'
    'https://www.budgetbytes.com/cranberry-apple-baked-oatmeal/'
    'https://www.budgetbytes.com/creamy-garlic-chicken/'
    )

#------------
# Size of array
#------------
size=${#URLs[@]} 

#------------
# For each url, run retrieval script
#------------
for (( i-0; i < $size; i++ ))    
{
    extract_scripts/retrieveURL.sh ${URLs[$i]}
}
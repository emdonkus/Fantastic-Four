#!/bin/bash
filepath='Recipes/budgetbytes/Apple_Cranberry_Baked_Oatmeal/Apple_Cranberry_Baked_Oatmeal_ingredients.txt'
ls $filepath
if [[ -s $filepath ]];
then
    echo "GOOD"
else
    echo "BAD"
fi

# build directory heirarchy for recipe
# call dir.sh with name of recipe to build hierarchy

#!bin/bash

if [ -z "$1" ]; then
	echo "Please enter the recipe name to build a directory."
	exit 1
fi

RNAME="$1"

if [ -d Recipes ]; then 
	cd Recipes

else
	mkdir Recipes
	echo "Created Recipes directory."
	cd Recipes

fi


if [ -d $RNAME ]; then
	echo "$RNAME directory already exists"
	ls "$RNAME"
else
	mkdir $RNAME
	echo "Created $RNAME directory."
	cd $RNAME
fi

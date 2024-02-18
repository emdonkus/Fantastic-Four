#!/bin/bash
# Script:
#  dir.sh
#
# Purpose:
#   Build a directory hierarchy to store files for each recipe
#
# Inputs:
#   $1 = Recipe name
#
# Outputs:
#   Print what directory has been created
#
# Notes:
#   Assumes working directory is the home directory of the repository
#
# Exits
#   0 = success
#   1 = no name entered for directory creation
#    
# Changelog:
#    Date (MM-DD-YYYY)     Name      Change Description
#    02-18-2024            halleeray   Initial Creation
#
#------------------------------------------------------------------
#------------------------------------------------------------------


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

#!/bin/bash -x
# Script:
#  extractInstructions.sh
#
# Purpose:
#   extract the instructions from recipe
#
# Inputs:
#   Recipe print URL
#
# Outputs:
#   extracted text file
#
# Notes:
#   
#
# Exits
#   0 = success
#   1 = bad url
#   2 = bad grep 
#   3 = missing file
#    
# Changelog:
#    Date (MM-DD-YYYY)     Name      Change Description
#    02-16-2024            EDonkus   Initial Creation
#
#------------------------------------------------------------------
#------------------------------------------------------------------

grep -E *"instruction-text







echo "Extracion Complete"
exit 0
# Script:
#  dataParser.py
#
# Purpose:
#   Process extracted instructions html for just the instructions
#
# Inputs:
#   full_file_name to data, assumes called from above Recipe Dir
#
# Outputs:
#   Instructions Text
#
# Notes:
#   
#
# Exits
#    NA
#    
# Changelog:
#    Date (MM-DD-YYYY)     Name      Change Description
#    02-17-2024            EDonkus   Initial Creation
#
#------------------------------------------------------------------
#------------------------------------------------------------------

from html.parser import HTMLParser #Basis for python, used to parse through HTML
import sys #used to read in command line inputs, ie when called from bash script
import os
##-----------------------
## HTML Parser reads in  an html file and parses between data and tags
#-----------------------
DEBUG=1
class MyHTMLParser(HTMLParser):
    #--------------
    # Init function, create empty datalist
    #--------------
    def  __init__(self):
        HTMLParser.__init__(self)
        self.dataList=[]
    
    #---------------
    # Tells Feed function what to do with start tags
    #---------------
    def handle_starttag(self, tag, attrs):
        if(DEBUG==1):
            print("Encountered a start tag:", tag)
        else:
            return
    
    #---------------
    # Tells Feed function what to do with end tags
    #---------------
    def handle_endtag(self, tag):
        if(DEBUG==1):
            print("Encountered an end tag :", tag)
        else:
            return
    
    #---------------
    # Tells Feed function what to do with data
    #---------------
    def handle_data(self, data):
        if(DEBUG==1):
            print("Data :", data)
            
        self.dataList.append(data)
        
    #---------------
    # Removes empty strings from dataList
    #---------------
    def trimDataList(self):
        self.dataList.remove('')
        
#--------------
# Debug print only if Global DEBUG is 1
#--------------
def dprint(input):
    if(DEBUG==1):
        print(str(input))
    #end if DEBUG
#end dprint

#-------------    
# Reassign input to var
#-------------
full_file_name = sys.argv[1]
dprint(full_file_name)

#-------------
# Make sure path exists
#-------------
if (os.path.exists(full_file_name) == False):
    exit(1)

#--------------
# Read in input file into variable
#--------------
with open(full_file_name, "r") as htmlfile:
    html_instructions=htmlfile.read()
    
#-------------
# Instantiate parser and run on instruction list, comes from imported lib
#-------------        
parser = MyHTMLParser()
parser.feed(html_instructions) 

#-------------
# Take dataList and write to file
#-------------
count = 1

#create new text filename
new_txt_file = full_file_name.replace(".html", ".txt")

#----------------
# Write parsed instructions to txt file with number
#----------------
with open(new_txt_file, "w") as outputFile:
    
    for step in parser.dataList:
        outputFile.write(str(count)+ ". "+step+"\n")
        count+=1


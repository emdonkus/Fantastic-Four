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
#    1 - missing file
#    2 - empty file
#    
# Changelog:
#    Date (MM-DD-YYYY)     Name      Change Description
#    02-17-2024            EDonkus   Initial Creation
#    03-07-2024            EDonkus   Updated script to account for various tags and different standards
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
        self.ingredient_list_flag=False
        self.instruction_list_flag=False
    
    #---------------
    # Tells Feed function what to do with start tags
    #---------------
    def handle_starttag(self, tag, attrs):
        if(DEBUG==1):
            print("Encountered a start tag:", tag)
        #end debug if
        text=HTMLParser.get_starttag_text(self)
        print(text)
        #---------------
        # If the start tag is a list with these in it, set the flag to true
        #---------------
        if ( '<ul class=' in text  and 'wprm-recipe-instructions' in text):
            if(DEBUG==1):                
                print("Setting instruction flag to true")
            self.instruction_list_flag=True
        elif ('<ul class=' in text and 'wprm-recipe-ingredients' in text):
            if(DEBUG==1):
                print("Setting ingredient flag to true")
            self.ingredient_list_flag=True
        #end tag if
        return
    #end handle_starttag
    
    #---------------
    # Tells Feed function what to do with end tags
    #---------------
    def handle_endtag(self, tag):
        if(DEBUG==1):
            print("Encountered an end tag :", tag)
        #end debug
        #---------------
        # If the flag is true set to false at /ul
        #---------------
        if ( 'ul' in tag and self.instruction_list_flag==True ):
            if(DEBUG==1):
                print("Setting instruction flag to false")
            self.instruction_list_flag=False
        elif ('ul' in tag and self.ingredient_list_flag==True):
            if(DEBUG==1):
                print("Setting ingredient flag to false")
            self.ingredient_list_flag=False
        #end tag if
    #end handle_endtag
    
    #---------------
    # Tells Feed function what to do with data
    #---------------
    def handle_data(self, data):
        if(DEBUG==1):
            print("Data :", data)
        #end debug
        
        #get last start tag    
        text=HTMLParser.get_starttag_text(self)
        if(DEBUG==1):
            print("Tag :", text)
        #end debug
        
        #if running on instructions, just add it to data
        if ( self.instruction_list_flag == True):
            if(DEBUG==1):
                print("Appending data for instruction list")
            #end debug
            
            # if last tag has recipe-inline-ingredient, append it to last item. 
            # This should also handle next lines where no new start tag was given
            if( "wprm-inline-ingredient" in text or data == ""):

                #Get the last element
                instructionSTR=self.dataList.pop()
                
                #Append data to string
                instructionSTR+=data
                
                #reinsert last element
                self.dataList.append(instructionSTR)
            elif("span" in text ):
                self.dataList.append(data)
            elif("a href=" in text):
                #Get the last element
                instructionSTR=self.dataList.pop()
                
                #Append data to string
                instructionSTR+=data
                
                #reinsert last element
                self.dataList.append(instructionSTR)
            
            else:
                self.dataList.append(data)

            

        elif (self.ingredient_list_flag ==True ):
            # if ingredient then we want to get the full line (2 onces chicken (thighs are good))
            # in one line and output the entire line to a single cell rather each part 
            # of list on a single line
            if(DEBUG==1):
                print("Appending data for ingredient list")
            #end debug
            if ( "unit" in text):
                # if unit is in text, save it to string
                
                #remove the last item
                ingredientSTR= self.dataList.pop()
                
                #append data to it
                ingredientSTR+=data
                
                #append ingredientSTR back to dataList
                self.dataList.append(ingredientSTR)

            elif ("amount" in text):
                # if amount in text, append to str
                
                # if the data string is empty, just add it to the last element string
                if ( data == " "):
                    #remove the last item
                    ingredientSTR= self.dataList.pop()
                    ingredientSTR+=data
                    self.dataList.append(ingredientSTR)
                else:
                    #Unit tag should start a new line of code
                    self.dataList.append(data)

                
            elif ( "name" or "ingredient-link" in text):
                # if amount in text, append to str
                #remove the last item
                ingredientSTR= self.dataList.pop()
                
                #append data to it
                ingredientSTR+=data
                
                #append ingredientSTR back to dataList
                self.dataList.append(ingredientSTR)
            elif ("notes" in text):
                # if amount in text, append to str
                #remove the last item
                ingredientSTR= self.dataList.pop()
                
                #append data to it
                ingredientSTR+=data
                
                #append ingredientSTR back to dataList
                self.dataList.append(ingredientSTR)
            #end ingredient datalist if
            if(DEBUG==1):
                print("Datalist: ")
                for item in self.dataList:
                    print(item)
                #end print loop
            #end debug
    #end handle_data
    
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

if(os.path.getsize(full_file_name) <= 0):
    exit(2)
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

#-------------
#create new text filename
#-------------
new_txt_file = full_file_name.replace(".html", ".txt")


#----------------
# Write parsed instructions to txt file with number
#----------------
with open(new_txt_file, "w") as outputFile:
    dprint("Writing to new file " + new_txt_file )
    for step in parser.dataList:
        dprint(step)
        outputFile.write(str(count)+ ". "+step+"\n")
        count+=1

if(os.path.getsize(new_txt_file) <= 0):
    exit(2)
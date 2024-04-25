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
import argparse
from Frontend import adding_data
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


def readhtmlfile(full_file_name):
    #--------------
    # Read in input file into variable
    #--------------
    with open(full_file_name, "r") as htmlfile:
        html_instructions=htmlfile.read()
    
    return html_instructions
#end readhtmlfile

def writetextfile(new_txt_file):
    #----------------
    # Write parsed instructions to txt file with number
    #----------------
    with open(new_txt_file, "w") as outputFile:
        dprint("Writing to new file " + new_txt_file )
        for step in parser.dataList:
            dprint(step)
            outputFile.write(str(count)+ ". "+step+"\n")
            count+=1
#end writetextfile

#--------------
# Writes text file to database
#---------------
def addToDatabase(recipe_name, new_txt_file, instruction_flag):
    #Conect to database
    conn = adding_data.connect_to_db()
    
    #Adding recipe to database, check if already there first
    if ( adding_data.check_recipe_exist(recipe_name) ):
        adding_data.insert_recipe(conn, recipe_name)
    else:
        exit(4)
    
    #if we are adding the instructions or ingredients, else exit out
    if (instruction_flag == 1):
        adding_data.insert_instructions(conn, new_txt_file, recipe_name)
    elif (instruction_flag == 2):
        adding_data.insert_ingredients(conn, new_txt_file, recipe_name)
    else:
        dprint(instruction_flag + " Not Valid")
        exit(3)
        
    conn.close()
#end addToDatabase

if __name__ == "__main__":
    #-------------    
    # Reassign input to var, validate it
    #-------------
    if (sys.argv[1]):
        full_file_name = sys.argv[1]
    else:
        exit(2)
        
    dprint(full_file_name)
    
    if (sys.argv[2]):
        instruction_flag = sys.argv[2]
    else:
        instruction_flag = -1
        
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
    html_instructions = readhtmlfile(full_file_name)   
    
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
    writetextfile(new_txt_file)
    
    #Extract recipe name from file path
    recipe_name = full_file_name.replace("_ingredients.html", "")
    recipe_name = recipe_name.split('/',1)[-1]
    
    dprint(recipe_name)
    

    addToDatabase(recipe_name,new_txt_file,instruction_flag)
    
    if(os.path.getsize(new_txt_file) <= 0):
        exit(2)
        
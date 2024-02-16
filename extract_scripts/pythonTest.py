from html.parser import HTMLParser

##-----------------------
## HTML Parser reads in  an html file and parses between data and tags
#-----------------------
class MyHTMLParser(HTMLParser):
    def  __init__(self):
        HTMLParser.__init__(self)
        self.dataList=[]
        
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Data :", data)
        self.dataList.append(data)
        
#-------------    
# Run shell script to get Instruction list into own html file
#-------------


#-------------
# Instantiate parser and run on instruction list
#-------------



#-------------
# Take dataList and write to file
#-------------



# Notes:
# Need to make sure python knows where files are being created
#  Might be a case for further separating bash script into separate bash scripts
#  
with open("temp.html", "r") as htmlfile:
    test=htmlfile.read()
        
parser = MyHTMLParser()
parser.feed(test)
count = 1
with open("Instructions.txt", "w") as outputFile:
    
    for step in parser.dataList:
        outputFile.write(str(count)+ ". "+step+"\n")
        count+=1
        
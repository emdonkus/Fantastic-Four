from html.parser import HTMLParser

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
        
    

with open("temp.html", "r") as htmlfile:
    test=htmlfile.read()
        
parser = MyHTMLParser()
parser.feed(test)
count = 1
with open("Instructions.txt", "w") as outputFile:
    
    for step in parser.dataList:
        outputFile.write(str(count)+ ". "+step+"\n")
        count+=1
        
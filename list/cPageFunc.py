import os

def cPage(fileName, PageName, DerictFirst, DerictSecond): #Function to add page for index category file

    os.mkdir(DerictFirst+"/"+DerictSecond)

    with open('cHT.txt', 'r') as cHT: #Open file with maket
        with open(DerictFirst+"/"+fileName+'.html', 'w') as cHM:
            for OHM in cHT:
                cHM.write(OHM)

    with open(DerictFirst+"/"+PageName+".html", "a") as apend: #To add addres in file
        apend.write("\n<div class=\"arContBlok\"><a href=\""+fileName+".html\"></a></div>")

    with open(DerictFirst+"/style/"+fileName+".css", "w") as writeStyle:  #Create style file for page
        writeStyle.write("/*Style " + fileName + "*/")

    with open(DerictFirst+"/"+fileName+".html", "r+") as addLink:#Link style with fileName
        addLink.seek(55)
        addLink.write("    <link rel=\"stylesheet\" href=\"style/"+fileName+".css\">")

def cPageAdd(fileName, PageName, DerictFirst, DerictSecond, NameLink): #The function of adding a file for a document added to the index category
    with open('MakAdPag.txt', 'r') as cHTadd: #Open file with maket
        with open(DerictFirst+"/"+DerictSecond+"/"+fileName+'.html', 'w') as cHM:
            for OHM in cHTadd:
                cHM.write(OHM)

    with open(DerictFirst+"/"+PageName+".html", "a") as apend: #To add addres in index file
        apend.write("\n<li><a href=\""+DerictSecond+"/"+fileName+".html\">"+NameLink+"</a></li>")

    with open(DerictFirst+"/style/"+fileName+".css", "w") as writeStyle: #Create style file for page
        writeStyle.write("/*Style " + fileName + "*/")

    with open(DerictFirst+"/"+DerictSecond+"/"+fileName+".html", "r+") as addLink: #Link style with fileName
        addLink.seek(55)
        addLink.write("<link rel=\"stylesheet\" href=\"../style/"+fileName+".css\">")

    with open(DerictFirst+"/"+DerictSecond+"/"+fileName+".html", "a") as addLink: #Link style with fileName
        addLink.write("<a href=\"../"+PageName+".html\">"+PageName+"</a>")

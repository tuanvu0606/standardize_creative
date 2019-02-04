import os
from bs4 import BeautifulSoup
import shutil
import fnmatch
from glob import glob
# print(os.path.isdir("/home/el"))
# print(os.path.exists("/home/el/myfile.txt"))

exist = True

def open_and_write_to_html_file(html_file,written_object):
    f= open(html_file,"w+")
    f.write(written_object)
    f.close()

stylesheet_path = str(os.getcwd()) + "/css"
html_file = str(os.getcwd()) + "/index.html"

html = open(html_file).read()
soup = BeautifulSoup(html, features="html.parser")

script_tag_with_src = soup.find_all("script",{"src":True})

for script in script_tag_with_src:
	print(script["src"])
	if script["src"].find("http") == -1:
		if script["src"].find("/") == -1:
			print ("JS script source is in current folder, leave it")
		else:
			print ("JS script source is in local folders as found in: " + script["src"] + ", bring it to the workspace, destroy the folder")
			shutil.move(os.getcwd() + "/" + script["src"], os.getcwd())
			print ("now modify the html file to use new .js file in workspace")
			print (script["src"][script["src"].index("/") + len("/"):])
			script["src"] = (script["src"][script["src"].index("/") + len("/"):])
			open_and_write_to_html_file(html_file,str(soup.prettify()))
	else:
		print ("JS script source is on the Internet, leave it")

stylesheet = soup.find_all(rel="stylesheet")

if not stylesheet:
    print ("no stylesheet link")
    print ("creating stylesheet file...")
    f= open("style.css","w+")
    f.write("/* begin of file */")
    f.close() 
    print ("creating stylesheet tag...")

    new_stylesheet_link = soup.new_tag('link', rel="stylesheet", href="style.css")
    print (new_stylesheet_link)
    soup.head.insert(2, new_stylesheet_link)

    # print(soup.prettify())

    f= open(html_file,"w+")
    f.write(str(soup.prettify()))
    f.close()

else:
    print("stylesheet link exist")
    # print (stylesheet[0].get('href'))
    # shutil.move(os.getcwd()str(stylesheet[0].get('href'), os.getcwd())
    print(os.getcwd() + "/" + str(stylesheet[0].get('href')))
    print("checking if stylesheet .css file is in subfolder...")

    print (str(stylesheet[0].get('href')).__contains__('/'))

    if str(stylesheet[0].get('href')).__contains__('/') == False:
        print(".css file is in current folder")
    else:
        if os.path.isfile(os.getcwd() + "/" + str(stylesheet[0].get('href'))) == True:
            print("stylesheet link is found with css file in" + os.getcwd() + "/" + str(stylesheet[0].get('href')))  
            print("moving .css file to current folder...")
            shutil.move(os.getcwd() + "/" + str(stylesheet[0].get('href')), os.getcwd())
            print("now modify index.html file to use new css file...")        
            new_stylesheet_location = str(stylesheet[0]['href'][stylesheet[0]['href'].index("/") + len("/"):])
            stylesheet[0]['href'] = new_stylesheet_location             
            print (stylesheet)
            open_and_write_to_html_file(html_file,str(soup.prettify()))          
        else:
            print("The css file does not exist, this file is corrupted")


image_link = soup.find_all("img")

if not image_link:
    print ("no image link")
  
else:
    for image in image_link:
        print(image["src"])
        if image["src"].find("http") == -1:
          if image["src"].find("/") == -1:
            print ("image source is in current folder, leave it")
            # print(os.path.isfile(os.getcwd() + "/" + image["src"]))
          else:
            # print(os.path.isfile(os.getcwd() + "/" + image["src"]))            
            if os.path.isfile(os.getcwd() + "/" + image["src"]) == True:
                print ("image source is in local folders as found in: " + image["src"] + ", bring it to the workspace")
                shutil.move(os.getcwd() + "/" + image["src"], os.getcwd())                
            else:
                print("image is in current workspace")
            print ("now modify the html file to use new image file in workspace")
            print (image["src"][image["src"].index("/") + len("/"):])
            image["src"] = (image["src"][image["src"].index("/") + len("/"):])
            open_and_write_to_html_file(html_file,str(soup.prettify()))
        else:
          print ("JS script source is on the Internet, leave it")




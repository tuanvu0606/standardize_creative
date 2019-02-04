import os
from bs4 import BeautifulSoup
import shutil
import fnmatch
from glob import glob
# print(os.path.isdir("/home/el"))
# print(os.path.exists("/home/el/myfile.txt"))

def JS_scraping(html_file):
    i = 0
    scraped_css_text = ""
    print ("begin scraping script element...")
    print (html_file)

    script_tag = soup.find_all("script")
    print (script_tag[0].string)
    print (len(script_tag[0].string))
    print (len("https://s3-ap-southeast-1.amazonaws.com/tuan.vu.yoose/The_Coffee_House/199/v4_tracking.js"))
    print("Checking if style_tag string length is greater than 91...")
    for script in script_tag:
        print (script)
        if (len(script.string) > 91):
              print("The style_tag string length is greater than 91...")
              print("Send it to external css file and delete the current one inside html file")                  
              f= open("YS" + str(i) + ".js","w+")
              f.write(script.string)
              f.close()
              script['src']="YS" + str(i) + ".js"
              script.string.replace_with("")     
              print("done removing")
              i = i + 1
        else:
            print("The style_tag string length is less than or equals 91...")
            print("keep it inside html_file")
    f= open(html_file,"w+")
    f.write(str(soup.prettify()))
    f.close()
def open_and_write_to_html_file(html_file,written_object):
    f= open(html_file,"w+")
    f.write(written_object)
    f.close()

stylesheet_path = str(os.getcwd()) + "/css"
html_file = str(os.getcwd()) + "/index.html"

html = open(html_file).read()
soup = BeautifulSoup(html, features="html.parser")

script_tag_with_src = soup.find_all("script",{"src":True})

# script = script_tag[0]

# print(script["src"])

for script in script_tag_with_src:
	print(script["src"])
	if script["src"].find("http") == -1:
		if script["src"].find("/") == -1:
			print ("JS script source is in current folder, leave it")
			JS_scraping(html_file)
		else:
			print ("JS script source is in local folders as found in: " + script["src"] + ", bring it to the workspace, destroy the folder")
			shutil.move(os.getcwd() + "/" + script["src"], os.getcwd())
			print ("now modify the html file to use new .js file in workspace")
			print (script["src"][script["src"].index("/") + len("/"):])
			script["src"] = (script["src"][script["src"].index("/") + len("/"):])
			open_and_write_to_html_file(html_file,str(soup.prettify()))
	else:
		print ("JS script source is on the Internet, leave it")

script_tag_without_src = soup.find_all("script",{"src":False})        

for script in script_tag_without_src:
    JS_scraping(html_file)
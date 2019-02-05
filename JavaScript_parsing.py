import os
from bs4 import BeautifulSoup
import shutil
import fnmatch
from glob import glob
import json
from pprint import pprint

def JS_scraping(html_file,script,i):
    print(str(i))
    print ("begin scraping script element...")
    print (html_file)
    with open('config.json') as f:
      data = json.load(f)

    creative_name = str(data["campaign"][0]["name"]) + "-" + str(data["DSP"]) + "-" + str(data["width"]) + "x" + str(data["height"]) 
    # script_tag = soup.find_all("script")



    print (len("https://s3-ap-southeast-1.amazonaws.com/tuan.vu.yoose/The_Coffee_House/199/v4_tracking.js"))
    print("Checking if style_tag string length is greater than 91...")
    print (script)
    if (len(script.string) > 91):
        print("The style_tag string length is greater than 91...")
        print("Send it to external css file and delete the current one inside html file")                  
        script_tag_name = creative_name + "-" + "YS" + str(i) + ".js" 
        f= open(script_tag_name,"w+")
        f.write(script.string)
        f.close()
        script['src']=script_tag_name
        script.string.replace_with("")     
        print("done removing")
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

def add_repo_to_script_tag(script):
  with open('config.json') as f:
    data = json.load(f)
  pprint(data)

  repo = str(data["repo"]) + "/" + str(data["campaign"][0]["name"]) + "/" + str(data["build"])

  print(repo)

  print(script['src'])
  script['src'] = repo + "/" + script['src'] 

  print(script['src'])


stylesheet_path = str(os.getcwd()) + "/css"
html_file = str(os.getcwd()) + "/index.html"

html = open(html_file).read()
soup = BeautifulSoup(html, features="html.parser")

script_tag_with_src = soup.find_all("script",{"src":True})

# script = script_tag[0]

# print(script["src"])

j = 0

for script in script_tag_with_src:
  print(script["src"])
  if script["src"].find("http") == -1:
    if script["src"].find("/") == -1:
      print ("JS script source is in current folder, leave it")
      JS_scraping(html_file,script,j)
      j = j + 1
    else:
      print ("JS script source is in local folders as found in: " + script["src"] + ", bring it to the workspace, destroy the folder")
      shutil.move(os.getcwd() + "/" + script["src"], os.getcwd())
      print ("now modify the html file to use new .js file in workspace")
      print (script["src"][script["src"].index("/") + len("/"):])
      script["src"] = (script["src"][script["src"].index("/") + len("/"):])
      open_and_write_to_html_file(html_file,str(soup.prettify()))
    add_repo_to_script_tag(script)
  else:
    print ("JS script source is on the Internet, leave it")

script_tag_without_src = soup.find_all("script",{"src":False})        

i = 0

for script in script_tag_without_src:    
    JS_scraping(html_file,script,i)
    i = i + 1
    add_repo_to_script_tag(script)
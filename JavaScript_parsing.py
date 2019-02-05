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

    print (len("https://s3-ap-southeast-1.amazonaws.com/tuan.vu.yoose/The_Coffee_House/199/v4_tracking.jsas"))
    print("Checking if style_tag string length is greater than 91...")
    print (script)
    if (len(script.string) > 91):
        print("The style_tag string length is greater than 91...")
        print("Send it to external css file and delete the current one inside html file")                  
        script_tag_name = "YS" + str(i) + ".js" 
        f= open(script_tag_name,"w+")
        f.write(script.string)
        f.close()
        script['src']=script_tag_name
        script.string.replace_with("")     
        print("done removing")
        add_repo_to_script_tag(script)
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

  print(script)

  repo = str(data["repo"]) + "/" + str(data["campaign"][0]["name"]) + "-" + str(data["width"]) + "x" + str(data["height"]) + "/" + str(data["DSP"]) + str(data["build"])

  print("repo: " + repo)

  print(""""script["src"]: """ + script["src"])
  script['src'] = (repo + "/" + script["src"] )

  print(script["src"])


stylesheet_path = str(os.getcwd()) + "/css"
html_file = str(os.getcwd()) + "/index.html"

html = open(html_file).read()
soup = BeautifulSoup(html, features="html.parser")

script_tag_with_src = soup.find_all("script",{"src":True})

# script = script_tag[0]

# print(script["src"])

print(script_tag_with_src)

j = 0
for script in script_tag_with_src:
  print(script["src"])
  if script["src"].find("http") == -1:    
    add_repo_to_script_tag(script)   
    # add_repo_to_script_tag(script)
    j = j + 1
  else:
    print ("JS script source is on the Internet, leave it")

script_tag_without_src = soup.find_all("script",{"src":False})        

i = 0

print(script_tag_without_src)

if script_tag_without_src:
  for script in script_tag_without_src:    
      JS_scraping(html_file,script,i)
      
      i = i + 1      
else:
  print("no script")
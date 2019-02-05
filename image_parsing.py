import os
from bs4 import BeautifulSoup
import shutil
import fnmatch
from glob import glob
import json
from pprint import pprint

html_file = str(os.getcwd()) + "/index.html"
html = open(html_file).read()
soup = BeautifulSoup(html, features="html.parser")

with open('config.json') as f:
  data = json.load(f)
pprint(data)

def add_repo_to_image(img):
  print ("begin adding repo to image")

  with open('config.json') as f:
      data = json.load(f)
  pprint(data)
  
  print (str(img['source']).__contains__('http'))

  if (str(img['source']).__contains__('http')) == True:
      print("image is pulled from the Internet, leave it")
  else:
      print("change the source of image to S3")
      repo = str(data["repo"]) + "/" + str(data["campaign"][0]["name"]) + "-" + str(data["width"]) + "x" + str(data["height"]) + "/" + str(data["DSP"]) + "/" + str(data["build"])

      img['source'] = (repo + "/" + img['source'])

      print(img['source'])

image_tag_source = data["image"]

for image_tag in image_tag_source:
    print(image_tag)
    image = soup.find_all(image_tag)
    if not image:
        print ("no image tag")
    else:
        print ("has image tag")	        
        exist_image = image
        for img in image:
            print(img["source"])
            add_repo_to_image(img)

f= open(html_file,"w+")
f.write(str(soup.prettify()))
f.close()
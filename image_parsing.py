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

image_tag_source = data["image"]

def add_repo_to_image(img,source):
  print ("begin adding repo to image")

  with open('config.json') as f:
    data = json.load(f)
  pprint(data)

  print(img)

  print(source)

  print (str(img[source]))

  print (str(img[source]).__contains__('http'))

  if (str(img[source]).__contains__('http')) == True:
      print("image is pulled from the Internet, leave it")
  else:      
      print("change the source of image to S3")
      repo = str(data["repo"]) + "/" + str(data["campaign"][0]["name"]) + "-" + str(data["width"]) + "x" + str(data["height"]) + "/" + str(data["DSP"]) + "/" + str(data["build"])
      img[source] = (repo + "/" + img[source])
      print(img[source])

# print (soup.find_all("img",{"src":True}))

for image_tag in image_tag_source:
  print(image_tag)    
  # source_image = soup.find_all(image_tag,{"source":True})
  # scr_image = soup.find_all(image_tag,{"source":True})
  if (soup.find_all(str(image_tag),{"src":True})):
    print("found src " + image_tag)
    for img in (soup.find_all(str(image_tag),{"src":True})):      
      add_repo_to_image(img,"src")
  elif (soup.find_all(str(image_tag),{"source":True})):
    print("found source " + image_tag)
    for img in (soup.find_all(str(image_tag),{"source":True})):      
      add_repo_to_image(img,"source")
  else:
    print("cant find image source")

  # print(soup.find_all(image_tag,{"src":True}))


  # if (soup.find_all(str(image_tag),{"scr":True})):
  #     print ("image src tag")        
  # elif (soup.find_all(str(image_tag),{"source":True})):
  #     print ("image source tag")	        
  # else:
  #     print ("no image source src")
      

f= open(html_file,"w+")
f.write(str(soup.prettify()))
f.close()


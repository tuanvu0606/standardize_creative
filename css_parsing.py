import os
from bs4 import BeautifulSoup
import shutil
import fnmatch
from glob import glob
import json
from pprint import pprint

def css_scraping(html_file,css_file):
  scraped_css_text = ""
  print ("start scraping style element...")
  print (html_file)

  style_tag = soup.find_all("style")
  print (style_tag[0].string)
  print (len(style_tag[0].string))
  print (len("https://s3-ap-southeast-1.amazonaws.com/tuan.vu.yoose/The_Coffee_House/199/v4_tracking.js"))
  print("Checking if style_tag string length is greater than 91...")
  for style in style_tag:
      # print (style.string)
      if (len(style.string) > 91):
          print("The style_tag string length is greater than 91...")
          print("Send it to external css file and delete the current one inside html file")
          scraped_css_text = scraped_css_text + "\n" + style.string
          style.string.replace_with("")          
      else:
          print("The style_tag string length is less than or equals 91...")
          print("keep it inside html_file")
  print ("scraped_css_text: " + scraped_css_text)
  if (scraped_css_text != ""):
      f= open("style.css","w+")
      f.write(scraped_css_text)
      f.close() 
  


  f= open(html_file,"w+")
  f.write(str(soup.prettify()))
  f.close()

def open_and_write_to_html_file(html_file,written_object):
    f= open(html_file,"w+")
    f.write(written_object)
    f.close()

def add_repo_to_style_tag():
  print ("begin adding repo to css link")

  stylesheet = soup.find_all(rel="stylesheet")
  with open('config.json') as f:
      data = json.load(f)
  pprint(data)
  
  for style in stylesheet:
    print(style)
    print (str(style.get('href')).__contains__('http'))
    if str(style.get('href')).__contains__('http') == False:
        print("Change the css source file to repo")
        repo = str(data["repo"]) + "/" + str(data["campaign"][0]["name"]) + "-" + str(data["width"]) + "x" + str(data["height"]) + "/" + str(data["DSP"]) + str(data["build"])
        print("repo: " + repo)
        print(""""style["href"]: """ + style["href"])
        style['href'] = (repo + "/" + style['href'] )
        print(style['href'])
    else:
        print (str(style.get('href')))
        print("style is in the Internet, leave it")

  f= open(html_file,"w+")
  f.write(str(soup.prettify()))
  f.close()

stylesheet_path = str(os.getcwd()) + "/css"
html_file = str(os.getcwd()) + "/index.html"

html = open(html_file).read()
soup = BeautifulSoup(html, features="html.parser")

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

    css_scraping(html_file,"style.css")

    print (soup)

    f= open(html_file,"w+")
    f.write(str(soup.prettify()))
    f.close()

else:
    print("stylesheet link exist")
    print(os.getcwd() + "/" + str(stylesheet[0].get('href')))
    print("checking if stylesheet .css file is in subfolder...")

    css_scraping(html_file,"style.css")

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
            css_scraping(html_file,"style.css")

add_repo_to_style_tag()
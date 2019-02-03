import os
from bs4 import BeautifulSoup
import shutil
import fnmatch
from glob import glob
# print(os.path.isdir("/home/el"))
# print(os.path.exists("/home/el/myfile.txt"))

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
          scraped_css_text = scraped_css_text + " " + style.string
      else:
          print("The style_tag string length is less than or equals 91...")
          print("keep it inside html_file")
  print ("scraped_css_text: " + scraped_css_text)
  if (scraped_css_text != ""):
      f= open("style.css","w+")
      f.write(scraped_css_text)
      f.close() 
stylesheet_path = str(os.getcwd()) + "/css"
html_file = str(os.getcwd()) + "/index.html"

# if os.path.isdir(stylesheet_path) == True:
#     print("found")  
# else:
#     print("not found")
#     try:
#         os.makedirs(stylesheet_path) 
#     except OSError:  
#         print ("Creation of the directory %s failed" % stylesheet_path)
#     else:  
#         print ("Successfully created the directory %s" % stylesheet_path)

 
# # load the file
# with open(html_file) as inf:
#     txt = inf.read()
#     soup = bs4.BeautifulSoup(txt)
# # create new link
# new_link = soup.new_tag("link", rel="icon", type="image/png", href="img/tor.png")
# # insert it into the document
# soup.head.append(new_link)
 
# # save the file again
# with open(html_file, "w") as outf:
#     outf.write(str(soup))


# print (glob.glob('*.py'))

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

    f= open(html_file,"w+")
    f.write(str(soup.prettify()))
    f.close()

    css_scraping(html_file,"style.css")
    # with open(html_file, "w") as file:
    #     file.write(str(soup))

else:
    print("stylesheet link exist")
    # print (stylesheet[0].get('href'))
    # shutil.move(os.getcwd()str(stylesheet[0].get('href'), os.getcwd())
    print(os.getcwd() + "/" + str(stylesheet[0].get('href')))
    print("checking if stylesheet .css file is in subfolder...")

    print (str(stylesheet[0].get('href')).__contains__('/'))

    if str(stylesheet[0].get('href')).__contains__('/') == False:
        print(".css file is in current folder")
        css_scraping(html_file,"style.css")
    else:
        if os.path.isfile(os.getcwd() + "/" + str(stylesheet[0].get('href'))) == True:
            print("stylesheet link is found with css file in" + os.getcwd() + "/" + str(stylesheet[0].get('href')))  
            print("moving .css file to current folder...")
            shutil.move(os.getcwd() + "/" + str(stylesheet[0].get('href')), os.getcwd())
            print("now modify index.html file to use new css file...")        
            stylesheet[0]['href'] = "style.css"
            print (stylesheet)
        else:
            print("The css file does not exist, this file is corrupted")
            css_scraping(html_file,"style.css")



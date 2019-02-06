import os
from bs4 import BeautifulSoup
import shutil
import fnmatch
from glob import glob

html_file = str(os.getcwd()) + "/index.html"

html = open(html_file).read()
soup = BeautifulSoup(html, features="html.parser")

V4_script_link = soup.new_tag('script', type="text/javascript", src="https://s3-ap-southeast-1.amazonaws.com/tuan.vu.yoose/Yoose_creative_scripts/Yoose_V4_tracking.js")

print (V4_script_link)
soup.body.insert(0, V4_script_link)

#Add variable to fill
V4_script_variable = soup.new_tag('script', type="text/javascript")

changing_variable = """
  var lats = []
  var lngs = []
  
  var imp_v4 = "";
  var click_v4 = "";

  var click_client = "";
  var imp_client = "";
  var platform_macro = "";

  var destination_url = "";
  var latitude_1 = parseFloat("");
  var longitude_1 = parseFloat(""); 
  """

V4_script_variable.append(changing_variable)
print (V4_script_link)
soup.body.insert(2, V4_script_variable)

print(soup)

f= open(html_file,"w+")
f.write(str(soup.prettify()))
f.close()
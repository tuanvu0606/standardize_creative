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
  var lats = [48.2109543,48.2019433,48.2025328]
  var lngs = [16.3767531,16.3698786,16.3620117]

  var nearest = 2000

  var imp_v4 = "";
  var click_v4 = "";

  var click_client = "";
  var imp_client = "";
  var platform_macro = "";

  var destination_url = "";
  var latitude_1 = parseFloat("");
  var longitude_1 = parseFloat(""); 

  var store_lat =0;
  var store_lng =0;
  var nearest = 0;
  var dist =0;
  var destination_location = "";
  var destination_url = "";


  function trackClick(){
  createImgEl(click_client);
  createImgEl(click_v4);
  createImgEl(platform_macro);
  window.open(destination_url);
  }
  function createImgEl(src) {
  var img = new Image(1,1);
  img.style.display = 'none';
  img.src = src;
  document.body.appendChild(img);
  }
  var m_u = "https://api.v4.yoose.com/";
  """

V4_script_variable.append(changing_variable)
print (V4_script_link)
soup.body.insert(0, V4_script_variable)

print(soup)

f= open(html_file,"w+")
f.write(str(soup.prettify()))
f.close()
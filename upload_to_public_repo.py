import os
from bs4 import BeautifulSoup
import shutil
import fnmatch
from glob import glob
import json
from pprint import pprint

with open('config.json') as f:
    data = json.load(f)

html_file = str(os.getcwd()) + "/index.html"

html = open(html_file).read()
soup = BeautifulSoup(html, features="html.parser")

pprint(data)

repo = str(data["repo"]) + "/" + str(data["campaign"][0]["name"]) + "/" + str(data["build"])

print(repo)
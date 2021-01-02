
# -*- coding:utf-8 -*-
import webbrowser
import requests
from bs4 import BeautifulSoup as bs
import re
import seaborn as sns

# gen url to jisho
def webInfo(kan):
    webstem = 'https://jisho.org/search/'
    suffix = ""
    k = str((kan).encode("utf-8"))
    kanji = k[2:-1]
    chars = "\\x"
    kanji = kanji.replace(chars, '%')
    webstring = webstem + kanji + suffix
    return webstring


# Load webpage content
def jlptGrade(webstring):
    r = requests.get(webstring)
    soup = bs(r.content, features="html.parser")
    try:
        n = soup.find("span", string=re.compile('(JLPT|jlpt)')).text
        grade = n.split(' ')[1]
    except:
        grade = 'NA'
    return grade


    
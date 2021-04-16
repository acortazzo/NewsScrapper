import pyperclip
import urllib.request
import webbrowser
import os
import codecs
from bs4 import BeautifulSoup

####### 1. Descargar html pasando una url

## Saco del clipboard la url copiada
NewsUrl = pyperclip.paste()

# Descargo la pagina
fid=urllib.request.urlopen('https://www.clarin.com/fama/error-edicion-programa-guido-kaczka-mostro-debia-ver-revelo-gran-secreto_0_GG2W-nU9p.html')
htmlnewsfull=fid.read().decode('utf-8')

#######  2. "scrapear" html y dejar solo el body 

soup = BeautifulSoup(htmlnewsfull, 'html.parser')
text = str(soup.find("div", {"class": "body-nota"}))


# string_corte = 'content-top-right'

string_corte = 'Mirá también'
try:
    texto_final = text[:text.index(string_corte)]
except IndexError:
    string_corte = 'content-top-right'
    try:
     texto_final = text[:text.index(string_corte)]
    except IndexError:
     texto_final = text[:text.index(string_corte)]

# texto_final = text[:text.index(string_corte) + len(string_corte)]

texto_final = text[:text.index(string_corte)]

####### 3. "Printear" el body depurado, y meterlo en otro html

f = codecs.open("nota.html", "w", "utf-8")
f.write(str(texto_final))
f.close()

####### 4. Abrir el html 

#  url = "file://d/testdata.html"

webbrowser.open_new_tab('nota.html')
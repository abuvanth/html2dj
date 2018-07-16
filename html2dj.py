from bs4 import BeautifulSoup
import os
import glob
files=glob.glob(os.getcwd()+"/"+"*.html")
for ft in files:
    htm=open(ft,'r')
    soup=BeautifulSoup(htm,'html.parser')
    for i in soup.find_all('script'):
        if i.has_attr('src'):
           if str(i['src']).startswith('assets'): # assets should be changed to js if the root folder of js file is 'js'
              i['src']="{% static '"+i['src']+"' %}"
    for j in soup.find_all('link'):
        if j.has_attr('href'):
           if str(j['href']).startswith('assets'): # assets should be changed to css if the root folder of css file is 'js'
              j['href']="{% static '"+j['href']+"' %}"
    for k in soup.find_all('img'):
        if k.has_attr('src'):
           if str(k['src']).startswith('assets'): # assets should be changed to images if the root folder of image file is 'images'
              k['src']="{% static '"+k['src']+"' %}"
    with open('dj-'+ft.split('/')[-1],'w') as fil:
         fil.write('{% load staticfiles %}\n'+str(soup))

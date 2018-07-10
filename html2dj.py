from bs4 import BeautifulSoup
import os
import glob
files=glob.glob(os.getcwd()+"/"+"*.html")
for ft in files:
    htm=open(ft,'r')
    soup=BeautifulSoup(htm,'html.parser')
    for i in soup.find_all('script'):
        if i.has_attr('src'):
           if str(i['src']).startswith('assets'):
              i['src']="{% static '"+i['src']+"' %}"
    for j in soup.find_all('link'):
        if j.has_attr('href'):
           if str(j['href']).startswith('assets'):
              j['href']="{% static '"+j['href']+"' %}"
    for k in soup.find_all('img'):
        if k.has_attr('src'):
           if str(k['src']).startswith('assets'):
              k['src']="{% static '"+k['src']+"' %}"
    with open('dj-'+ft.split('/')[-1],'w') as fil:
         fil.write('{% load staticfiles %}\n'+str(soup))

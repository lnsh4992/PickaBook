import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
from datetime import datetime as dt
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pickabook.settings")
import django
django.setup()
from books.models import Book
# import re


def tag_remove(HTML_string):
    
    removeList = ['<span class="details-content-text"> ','<b>','</b>','<i>','</i>','<p>','</p>','</span>', '<br>', '<br/>', '<span class="details-content-text">', '</strong>', '<strong>']
    
    clean_HTML = HTML_string
    for r in removeList:
        clean_HTML = clean_HTML.replace(r, '')
        
    return clean_HTML

def getPublishedDate(HTML_string):
    try:
        datePublished = str(HTML_string).split("<li><strong>Publish Date</strong>:")[1].split('</li>')[0][1:]
    except IndexError:
        return -1
    
    return datePublished

def parseInfo(HTML_string):
    
    genreList = ['FA','RO','TR','MY','BI','FI','NF', 'SF']
    
    clean_HTML = HTML_string.split('\"')
    clean_HTML = clean_HTML[1].split(':')
    
    author = clean_HTML[0]
    title = clean_HTML[1][1:]
    genre = genreList[random.randint(0,7)]
  
#    print(author)
#    print(title)

    return title, author, genre

def getDetail(link):
    req = requests.get(link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    
    

    
    overview = tag_remove(str(soup.select('span[class=details-content-text]')[0]))
    title, author, genre = parseInfo(str(soup.select('meta[property=og:title]')[0]))
    datePublished = getPublishedDate(soup.select('div[class="details-content-text"]'))
    
    if(datePublished == -1):
        return - 1
    
    datePublished = str(datePublished).split(' ')

    if "Jan" in datePublished[0]:
        datePublished[0] = "01"
    elif "Fe" in datePublished[0] :
        datePublished[0] = "02"
    elif "Mar" in datePublished[0] :
        datePublished[0] = "03"
    elif "Ap" in datePublished[0] :
        datePublished[0] = "04"
    elif "May" in datePublished[0] :
        datePublished[0] = "05"
    elif "Jun" in datePublished[0] :
        datePublished[0] = "06"
    elif "July" in datePublished[0] :
        datePublished[0] = "07"
    elif "Aug" in datePublished[0] :
        datePublished[0] = "08"
    elif "Sep" in datePublished[0] :
        datePublished[0] = "09"
    elif "Oct" in datePublished[0] :
        datePublished[0] = "10"
    elif "Nov" in datePublished[0] :
        datePublished[0] = "11"
    else:
        datePublished[0] = "12"

#    print(datePublished)

    datePublished = dt(int(datePublished[1]), int(datePublished[0]), 1, 0)

    return (title, author, genre, overview, str(datePublished).split(' ')[0])

def run():
    
    req = requests.get("https://www.booksamillion.com/new?oxid=8134b&oxname=newarrivals&oxpage=books&oxpos=navi&oxdate=062618")
    html = req.text
     
    soup = BeautifulSoup(html, 'html.parser')
    
    Books = {"Title":[], "Author":[], "Genre":[], "Link":[], "Image":[], "PbDate":[], "Overview":[], "Rating":[]}
    cnt = 0
    print("------------------------------------------------------")
    for tag in soup.select('div[class=img]'):
#         title = tag.a["title"]
        link = tag.a["href"]
        img = tag.img["src"]
        detail = getDetail(link)

        if(detail == -1):
            break  ## DVD section after this point

        cnt += 1
        print(cnt)
#        print("Title: ", detail[0])
#        print("Author: ", detail[1])
#        print("Genre: ", detail[2])
#        print("Link: ", link)
#        print("Image: ", img)
#        print("Date Published: ", detail[4])
#        print("Overview: ",detail[3])

        
        try:
            Book(title = detail[0], author_name = detail[1], publication_date = detail[4].split(' ')[0], genre = detail[2], rating = 0.0, image_url = img, synopsis = detail[3]).save()
        except:
#            print("Exception Occured!")
            continue

#        Books["Title"].append(detail[0])
#        Books["Author"].append(detail[1])
#        Books["Genre"].append(detail[2])
#        Books["Link"].append(link)
#        Books["Image"].append(img)
#        Books["PbDate"].append(detail[4])
#        Books["Overview"].append(detail[3])
#        Books["Rating"].append(0.0)

        print("------------------------------------------------------")


#    df = pd.DataFrame.from_dict(Books, orient="index")
#    df.to_csv("Books.csv")

if __name__ == '__main__':
    print("started!")
#    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")
#    django.setup()
    run()
        

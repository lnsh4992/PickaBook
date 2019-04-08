import json
import requests
from datetime import datetime as dt
import time
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pickabook.settings")
import django
django.setup()
from books.models import Book
import re
from bs4 import BeautifulSoup
from authors.models import Author


def tag_remove(HTML_string):
    
    removeList = ['<span class="details-content-text"> ','<b>','</b>','<i>','</i>','<p>','</p>','</span>', '<br>', '<br/>', '<span class="details-content-text">', '</strong>', '<strong>']
    
    clean_HTML = HTML_string
    for r in removeList:
        clean_HTML = clean_HTML.replace(r, '')
    
    return clean_HTML


def get_ImgBio(linkAuthor):
    req = requests.get(linkAuthor)
    htmlTxt = req.text
    soup = BeautifulSoup(htmlTxt, 'html.parser')
    
    getImg = soup.select('img["id"]')
    getBio = soup.select('p[class]')
    
    img = ""
    bio = ""
    
    for k in getImg:
        if("images-na.ssl-images-amazon.com" in k["src"]):
            img = str(k["src"])
            #            print(img)
            break

    getImg = None
    
    #    print("+++++++   ",len(getBio))

    if(len(getBio) > 2):
        getBio = str(getBio[0]) +  str(getBio[1]) + str(getBio[2])
        getBio = tag_remove(getBio.split("</p><p class")[0])
        #        print(getBio.split('>')[1])
        bio = getBio.split('>')[1]

        if(bio[0] == '\n'):
            bio = bio[1:]


    else:
        #        getBio = "Bio not provided"
        bio = "Bio not provided"


    return img, bio

def get_AuthorInfo(authName, searchResult):
    linkAudible = "https://www.audible.com"
    linkAudibleSearch = "https://www.audible.com/search?keywords=" + authName.replace(' ', '+')
    #    print(linkAudibleSearch)
    
    req = requests.get(linkAudibleSearch)
    htmlTxt = req.text
    soup = BeautifulSoup(htmlTxt, 'html.parser')
    authLink = soup.select('a["class"]')
    
    foundFlag = 0
    
    for k in authLink:
        if("/author/" in str(k["href"])):
            authLink =str(k["href"])
            #            print(str(k["href"]))
            foundFlag = 1;
            break

    if(foundFlag == 0):
        print("Not found!\n\n")
    else:
        linkAuthor = linkAudible + authLink
        print(linkAuthor)
        img, bio = get_ImgBio(linkAuthor)
        searchResult["image_url"] = img
        searchResult["bio"] = bio


    return searchResult


def get_ReviewInfo(bookTitle, searchResult):
    
    reviewInfo = BookReview.objects.values()
    
    for r in reviewInfo:
        if(r["title"] == bookTitle):
            searchResult["review"] = r["review"]


    return searchResult;


def getBookinfo(fullPath):
    req = requests.get(fullPath)
    jsonText = req.text
    jsonDic = json.loads(jsonText)
    return jsonDic



def crawlAuthor(isbn, authName, gen, bTitle):
    
#    print("@@@@@@@@@@@  isbn = ",isbn, authName, gen)

#    if(("XXXXX" not in isbn) and ("None" not in isbn)):
    authorName = authName
    searchResult = {"name":authorName, "genre":gen, "numFollowers":0, "review_count":0, "review":0.0, "image_url":0, "bio":0}
#        print(b["isbn"])
#    print(searchResult)
    if(re.search(r'\b' + "and" + r'\b', authorName)):
            authorName = authorName.split("and")[1][1:]
#            print(authorName)

#    print("@@@@@@@@\n")

#    searchResult = get_ReviewInfo(bTitle, searchResult)
    searchResult = get_AuthorInfo(authorName, searchResult)
                
    print(searchResult)

    try:
#        print("Author regisfsdfdsfdsf", len(searchResult["bio"]))
        Author(name = str(searchResult["name"]), image_url = str(searchResult["image_url"]),review_count = int(searchResult["review"]), bio = str(searchResult["bio"]), genre = str(searchResult["genre"]), numFollowers = str(searchResult["numFollowers"]), review = int(searchResult["review"])).save()
    except:
        return
#        print("Exception Occured! (Author)")


def crawl(path, api_key):
    
    #    fullPath = "https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=VwopaxgQABehBoAWn5YrwPL8j54rRuQB"
    
    genres = {"FA":"relationships", "RO":"relationships", "TR":"hardcover-graphic-books", "MY":"crime-and-punishment", "BI":"celebrities", "FI":"hardcover-fiction", "NF":"hardcover-nonfiction", "SF":"science"}
    
    for key in genres:
        fullPath = path + genres[key] + api_key
        
        load_Flag = 0
        
        while(load_Flag != 1):
            try:
                jsonDic = getBookinfo(fullPath)
                print("%s has %d new books." %(key, jsonDic["num_results"]))
                print("------------------------------------")
                load_Flag = 1
            except KeyError:
                print("%s did not work, try again." %key)
                load_Flag = 0
                time.sleep(3)
    
        date = jsonDic["last_modified"].split('T')[0]
        date = date.split('-')
        date = dt(int(date[0]), int(date[1]), 1, 0)
        print(str(date).split(' ')[0])
        
        bookInfo = jsonDic["results"]["books"]
        
        cnt = 0
        for b in bookInfo:
            try:
                Book(title = b["title"], author_name = b["author"], publication_date = str(date).split(' ')[0], genre = key, rating = 0.0, image_url = b["book_image"], synopsis = b["description"], isbn = str(b["primary_isbn10"])).save()
            
                crawlAuthor(str(b["primary_isbn10"]), b["author"], key, b["title"])
                cnt += 1
            except:
#                print("Exception Occured! (crawl)")
                continue
        
        print("%d books were updated from %s" %(cnt, key));

    print("===========================\n\n")


def run():
    path = "https://api.nytimes.com/svc/books/v3/lists/current/"
    key = ".json?api-key=VwopaxgQABehBoAWn5YrwPL8j54rRuQB"
    crawl(path, key)

#if __name__ == "__main__":
#    
#    path = "https://api.nytimes.com/svc/books/v3/lists/current/"
#    key = ".json?api-key=VwopaxgQABehBoAWn5YrwPL8j54rRuQB"
#    crawl(path, key)

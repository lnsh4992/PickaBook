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


def getBookinfo(fullPath):
    req = requests.get(fullPath)
    jsonText = req.text
    jsonDic = json.loads(jsonText)
    return jsonDic

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
                cnt += 1
            except:
                print("Exception Occured!")
                continue

        print("%d books were updated from %s" %(cnt, key));

        print("===========================\n\n")

if __name__ == "__main__":
    
    path = "https://api.nytimes.com/svc/books/v3/lists/current/"
    key = ".json?api-key=VwopaxgQABehBoAWn5YrwPL8j54rRuQB"
    crawl(path, key)
    
#    bookInfo = Book.objects.values()
#    for key in bookInfo:
#        print(key)


#dt(int(datePublished[1]), int(datePublished[0]), 1, 0)

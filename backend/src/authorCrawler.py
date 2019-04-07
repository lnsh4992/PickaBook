import os
#import json
import requests
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pickabook.settings")
import django
django.setup()
from books.models import Book
#from books.authors import Author
from reviews.models import BookReview
from bs4 import BeautifulSoup
import re
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


if __name__ == "__main__":
    
#    search(keyWords)

    bookInfo = Book.objects.values()

    for b in bookInfo:
        isbn = b["isbn"]

        if(("XXXXX" not in isbn) and ("None" not in isbn)):
            searchResult = {"name":b["author_name"], "genre":b["genre"], "numFollowers":0, "review_count":0, "review":0, "image_url":0, "bio":0}
#            print(b["isbn"])

            authorName = b["author_name"]
            if(re.search(r'\b' + "and" + r'\b', authorName)):
                authorName = authorName.split("and")[1][1:]
            print(authorName)
            
            
            searchResult = get_ReviewInfo(b["title"], searchResult)
            searchResult = get_AuthorInfo(authorName, searchResult)

            print(searchResult)

#            try:
            Author(name = str(searchResult["name"]), image_url = str(searchResult["image_url"]), review_count = int(searchResult["review"]), bio = str(searchResult["bio"]), genre = str(searchResult["genre"]), numFollowers = int(searchResult["numFollowers"]), review = 0.0).save()
#            except:
#                print("Exception Occured! (Author)")
#                continue


#            break;




#    fullPath = "https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=VwopaxgQABehBoAWn5YrwPL8j54rRuQB"
#    req = requests.get(fullPath)
#    jsonText = req.text
#    jsonDic = json.loads(jsonText)
#
#    for key in jsonDic["results"]["books"]:
#        print(key)

import numpy as np
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pickabook.settings")
import django
django.setup()
from books.models import Book

#def test(csvPath):

# Trim parsed keyword so that it contains only required information.
def preProcess_Keywords(keyWords):
    
    keyWords = keyWords.lower()
    keyWords = keyWords.replace('.', '')
    keyWords = keyWords.replace(',', '')
    keyWords = keyWords.replace(';', '')
    keyWords = keyWords.split(' ')
    
    rmvDuplicate = list(set(keyWords))
    
    for i in range(0, len(rmvDuplicate)):
        if(rmvDuplicate[i] == ''):
            del rmvDuplicate[i]
            break

    return rmvDuplicate


def search(keyWords):
    #    get books info from our database.
    bookInfo = Book.objects.values()
    
    title = []
    author_name = []
    
    cnt = 0
    for b in bookInfo:
    # To avoid getting frame inforamtaion (first element is fram info)
        if(cnt > 0):
            title.append(b["title"])
            author_name.append(b["author_name"])
        cnt += 1

    #    trim keyword before parse required information.
    trimedKeys = preProcess_Keywords(keyWords)
    keyWords = keyWords.lower()
    
#    print(keyWords)
#    print(trimedKeys)

    resultTitle = []
    rmvTitle = []
    resultAuthor = []
    
#    for searching robustness, change input/trimed data to lower cases
    for i in range(0, len(title)):
        matchCnt = 0
        for j in range(0, len(trimedKeys)):
            if(title[i].lower().find(trimedKeys[j]) != -1):
                    matchCnt += 1

        if(matchCnt > 0):
            if(len(trimedKeys) == len(title[i].split(' '))):
                if(title[i].lower().find(keyWords) != -1):
                    matchCnt = 100
            resultTitle.append((bookInfo[i + 1], matchCnt))
        else:
            rmvTitle.append(bookInfo[i + 1]["title"])
        


#    for searching robustness, change input/trimed data to lower cases
    for i in range(0, len(author_name)):
        matchCnt = 0
        for j in range(0, len(trimedKeys)):
            if(author_name[i].lower().find(trimedKeys[j]) != -1):
                matchCnt += 1
    
        if(matchCnt > 0):
            if(author_name[i].lower().find(keyWords) != -1):
                if(author_name[i].lower().find(keyWords) != -1):
                    matchCnt = 100
        
            resultAuthor.append((bookInfo[i + 1], matchCnt))



    for t in rmvTitle:
        bookInfo = bookInfo.exclude(title=t)

    bookInfo = bookInfo.exclude(title="Test book 1")

# Sorting to whoe high match rate result show first
    resultTitle.sort(key=lambda x: x[1], reverse=True)
    resultAuthor.sort(key=lambda x: x[1], reverse=True)

    tempT = resultTitle
    tempA = resultAuthor

    resultTitle = None
    resultAuthor = None
    resultTitle = []
    resultAuthor = []
    # print(tempT)

    for t in tempT:
        resultTitle.append(t[0])

    for t in tempA:
        resultAuthor.append(t[0])


#   If there are matched result print out Matched title and author.
    if((len(resultTitle) + len(resultAuthor)) == 0):
        print("Not Found!")
    # else:
    #     if(len(resultTitle) > 0):
    #         print("-------------- Matched Title --------------")
    #         for rT in resultTitle:
    #             # print(rT[0])
    #             print(rT)
    #         print("-----------------------------------------\n")
    #         # return resultTitle

        # if(len(resultAuthor) > 0):
        #     print("-------------- Matched Author --------------")
        #     for rA in resultAuthor:
        #         # print(rT[0])
        #         print(rA)
        #     print("-----------------------------------------\n")


    # print("@@@@@@@@@@@@@@@@@")
    # print(bookInfo)
    # print("@@@@@@@@@@@@@@@@@")

    return bookInfo


# if __name__ == "__main__":
    
#     keyWords = "of"
#     search(keyWords)


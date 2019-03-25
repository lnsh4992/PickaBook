import pandas as pd
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pickabook.settings")
import django
django.setup()
from books.models import Book


def test(csvPath):
    
    bookInfo = pd.read_csv(csvPath)
    
    cnt = 0
    
    titleL = []
    author_nameL = []
    publication_dateL = []
    genreL = []
    ratingL = []
    image_urlL = []
    synopsisL = []
    
    
    cnt = 0
    for key in bookInfo:
#        print(bookInfo[key])
        if(cnt > 0):
            titleL.append(bookInfo[key][0])
            author_nameL.append(bookInfo[key][1])
            genreL.append(bookInfo[key][2])
            image_urlL.append(bookInfo[key][4])
            publication_dateL.append(bookInfo[key][5])
            synopsisL.append(bookInfo[key][6])
            print(bookInfo[key][6])
            ratingL.append(bookInfo[key][7])
        cnt += 1
    
#    print(len(synopsis))


    for i in range(0, len(titleL)):
#        print(publication_dateL[i])
        print(publication_dateL[i].split(' ')[0])
        print()
#        try:
#            Book(title = titleL[i], author_name = author_nameL[i], publication_date = publication_dateL[i].split(' ')[i], genre = genreL[i], rating = ratingL[i], image_url = image_urlL[i], synopsis = synopsisL[i]).save()
#        except:
#            continue


if __name__ == "__main__":

    test("Books.csv")

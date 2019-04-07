import time
import datetime
import book_authorCrawler
from bs4 import BeautifulSoup
def run():

    print("runUpdator called!")
    
    while(1):
        
        today = datetime.datetime.today().weekday()
        if((today % 7) == 0):
            book_authorCrawler.run()
        
        time.sleep(3600)

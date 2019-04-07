import time
import datetime
import book_authorCrawler
from bs4 import BeautifulSoup
def run():

    print("runUpdator called!")
    
    started_day = datetime.datetime.today().weekday()
    
    while(1):
        
        if((started_day % 7) == 0):
            book_authorCrawler.run()
        
        time.sleep(3600)

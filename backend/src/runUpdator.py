import time
import book_authorCrawler

def run():

    print("runUpdator called!")
    
    countWeek = 7
    
    while(1):

        if(countWeek == 7):
            print(countWeek)
            countWeek = 0
            print(countWeek)
            book_authorCrawler.run()

        time.sleep(24 * 3600)
        countWeek += 1

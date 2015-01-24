# Comparitively Slow on Koding
from bs4 import BeautifulSoup
import urllib
import re
def indiatimes(isbn):
    #indiatimes shopping price fetch
    it_link="http://shopping.indiatimes.com/books/p_U"+isbn
    print it_link
    it_soup = BeautifulSoup(urllib.urlopen(it_link).read())
    it_temp = it_soup.find(property="og:price:amount")
    if(it_temp):
        it_regex=re.search('(\d{1,3},?)*\d{1,3}',str(it_temp))
        it_price=str(int(it_regex.group(0))-50)
        it_availtemp = BeautifulSoup(str(it_soup.find(property="og:availability"))).meta['content']
        if(it_availtemp=="instock"):
            it_avail="Available"
        else:
            it_avail="Out Of Stock"
    else:
        it_price="NA"
        it_avail="NA"
    print "Indiatimes finished"
    return [it_price,it_avail,it_link]
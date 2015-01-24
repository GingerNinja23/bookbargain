# Pretty Fast on Koding
from bs4 import BeautifulSoup
import urllib
import re
def bookadda(isbn):
    #Bookadda Price Fetch
    b_link = "http://www.bookadda.com/general-search?searchkey="+isbn
    print b_link
    b_soup = BeautifulSoup(urllib.urlopen(b_link).read())
    b_temp = (b_soup.find_all(itemprop="price"))
    if(b_temp):
        b_temp=b_temp[0]
        b_regex = re.search('\d+',str(b_temp))
        b_price = b_regex.group(0)
        b_availtemp = b_soup.select(".stckdtls")
        b_avail=re.search('Available|Out Of Stock|Pre-Order|Imported Edition',str(b_availtemp)).group(0)
        if b_avail=="Imported Edition":
            b_avail="Available"
    else:
        b_price = "NA"
        b_avail ="NA"
    blist =[b_price,b_avail,b_link]
    print "bookadda finished"
    return blist
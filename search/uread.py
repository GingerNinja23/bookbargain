from bs4 import BeautifulSoup
import urllib2
import re
def uread(isbn):
    u_link = "http://www.uread.com/search-books/"+isbn
    u_soup = BeautifulSoup(urllib2.urlopen(u_link).read())
    u_temp = u_soup.find(id="ctl00_phBody_ProductDetail_lblourPrice")
    if(u_temp):
    	#Find price using Regex
    	u_regex = re.search('\d+',str(u_temp))
    	u_price = u_regex.group(0)
    	u_availtemp = u_soup.find(id="ctl00_phBody_ProductDetail_lblAvailable")
    	u_availregex = re.search('Available|Out Of Stock',str(u_availtemp))
    	u_avail = u_availregex.group(0)
    else:
    	u_price="NA"
    	u_avail="NA"
    return [u_price,u_avail]
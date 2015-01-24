from bs4 import BeautifulSoup
import urllib
import re
import pyisbn
def amazon(isbn):
    #Amazon price fetch 
    isbn=pyisbn.convert(isbn)
    a_link="http://www.amazon.in/dp/"+isbn
    print a_link
    a_soup = BeautifulSoup((urllib.urlopen(a_link)).read())
    a_temp=a_soup.find(id="actualPriceValue")
    if(a_temp):
    	a_regex = re.search('(\d{1,3},?)*\d{1,3}\.\d{2}',str(a_temp))
    	a_price=a_regex.group(0)
    	if(a_soup.select(".availGreen")):
    	    a_avail = "Available"
    	if(a_soup.select(".availOrange")):
    	    a_availtemp=a_soup.select(".availOrange")[0]
    	    a_availtemp2=re.search('>[\w\s,.$><?@#$%^&*()_-]+<',str(a_availtemp)).group(0)[1:-1]
    	    if 'released' in a_availtemp2 :
    	        a_avail = "Pre-Order"
    	    else:
    	        a_avail = "Available"
    	if(a_soup.select(".availRed")):
    	    a_avail = "Out Of Stock"
    else:
    	a_price="NA"
    	#a_avail="Cannot Find On Amazon"
    	a_avail="Out Of Stock"
    alist = [a_price,a_avail,a_link]
    print "Amazon Finished"
    return alist

from bs4 import BeautifulSoup
import urllib
import re
def infibeam(isbn):
	#Infibeam Price Fetch
	ib_link = "http://www.infibeam.com/search.jsp?query="+isbn
	print ib_link
	ib_soup = BeautifulSoup(urllib.urlopen(ib_link).read())
	ib_temp = ib_soup.select(".infiPrice")
	if(ib_temp):
	    ib_temp=ib_temp[0]
	    ib_regex = re.search('(\d{1,3},?)*\d{1,3}',str(ib_temp))
	    ib_price = ib_regex.group(0)
	    ib_availtemp=ib_soup.select(".status")[0]
	    if(re.search('In Stock|Imported Edition',str(ib_availtemp))):
	        ib_avail="Available"
	    else:
	        ib_avail="Out of Stock"
	else:
	    ib_price="NA"
	    ib_avail="NA"
	iblist = [ib_price,ib_avail,ib_link]
	print "Infibeam finished"
	return iblist
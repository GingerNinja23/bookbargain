# Very slow on koding server
from bs4 import BeautifulSoup
import urllib2
import re
def landmark(isbn):
	# landmark price fetch
	l_link = "http://www.landmarkonthenet.com/books/search/?q="+isbn
	l_soup = BeautifulSoup(urllib2.urlopen(l_link).read())
	l_temp = l_soup.select(".price-current")
	if(l_soup.select(".instock")):
		#l_avail
		l_avail="Available"
	elif(l_soup.select(".cross")):
		l_avail="Out of Stock"
	else:
		l_avail="Cannot find on landmark"
	if(l_temp):
		l_temp=l_temp[0]
		l_regex=re.search('(\d{1,3},?)*\d{1,3}',str(l_temp))
		l_price = l_regex.group(0)
	else:
		l_price="Cannot find on landmark"
		l_avail="Cannot find on landmark"
	return [l_price,l_avail]
from bs4 import BeautifulSoup
import urllib
import re
def hs18(isbn):
	#Homeshop18 price fetch.

	h_link = "http://www.homeshop18.com/search:"+isbn
	print h_link
	h_soup=BeautifulSoup(urllib.urlopen(h_link).read())
	h_temp = h_soup.find_all(id='hs18Price')
	if (not h_temp):
		#h_price="unavailable"
		#h_price="Cannot Find on HS18"
		#h_avail="Cannot Find on HS18"
		h_price="NA"
		h_avail="NA"
	else:
		h_temp = h_temp[0]
		h_regex = re.findall('[1-9]\d*',str(h_temp.contents))
		h_price=h_regex[0]
		if(h_soup.select(".in_stock")):
		    h_avail="Available"
		else:
		    h_avail="Out of Stock"
	hlist = [h_price,h_avail,h_link]
	print "Homeshop18 finished"
	return hlist


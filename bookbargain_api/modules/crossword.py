import urllib2
from bs4 import BeautifulSoup
import time
import mechanize
import re
import pyisbn

def crossword(isbn):
	#Getting the Source
	start_time = time.time()
	if len(isbn) == 10:
		c_link = "http://www.crossword.in/books/search?q="+pyisbn.Isbn10(isbn).convert(code='978')
	else:
		c_link = "http://www.crossword.in/books/search?q="+isbn
	br = mechanize.Browser()
	br.set_handle_robots(False)   # ignore robots
	br.set_handle_refresh(False)  # can sometimes hang without this
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]# [('User-agent', 'Firefox')]
	try:
		response = br.open(c_link)
	except Exception, e:
		c_price="NA"
		return {'price':c_price,'url':c_link}

	#Creating the soup

	c_soup = BeautifulSoup(response.read())
	c_temp = c_soup.find_all("span",class_='variant-final-price')
	if(c_temp):
		c_temp = re.findall(r'R</span> (.*?)\n.*</span>',str(c_temp[0]))
		if(c_temp):
			c_price=c_temp[0]
		else:
			c_price="NA"
	else:

		c_price = "NA"

	return {'price':c_price,'url':c_link}

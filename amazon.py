import urllib2
from bs4 import BeautifulSoup
import pyisbn
import re
import time
import mechanize
def amazon(isbn):
	# isbn = '9789380501932'
	if len(isbn) == 13:
		a_link = "http://www.amazon.in/dp/"+pyisbn.Isbn(isbn).convert(code='978')
	else:
		a_link = "http://www.amazon.in/dp/"+isbn
	br = mechanize.Browser()
	#br.set_all_readonly(False)    # allow everything to be written to
	br.set_handle_robots(False)   # ignore robots
	br.set_handle_refresh(False)  # can sometimes hang without this
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]           # [('User-agent', 'Firefox')]
	response = br.open(a_link)
	a_soup = BeautifulSoup(response.read())
	a_class = a_soup.findAll('span',class_="price3P")[0]
	a_price = re.findall(r'</span> (.*?)</span>',str(a_class))[0]
	return a_price
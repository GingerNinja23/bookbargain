import urllib2
from bs4 import BeautifulSoup
import pyisbn
import re
import time
import mechanize
def landmark(isbn):
	if len(isbn) == 10:
		l_link = "http://www.landmarkonthenet.com/books/search/?q="+pyisbn.Isbn10(isbn).convert(code='978')
	else:
		l_link = "http://www.landmarkonthenet.com/books/search/?q="+isbn
	br = mechanize.Browser()
	#br.set_all_readonly(False)    # allow everything to be written to
	br.set_handle_robots(False)   # ignore robots
	br.set_handle_refresh(False)  # can sometimes hang without this
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]           # [('User-agent', 'Firefox')]
	try:
		response = br.open(l_link)
	except Exception, e:
		return {'price':'NA','url':l_link}
	l_soup = BeautifulSoup(response.read())
	l_class = l_soup.findAll('span',class_='price-current')
	if not l_class:
		return {'price':'NA','url':l_link}
	else:
		l_class = l_class[0]
	try:
		l_price = re.findall(r'Rs</span>(.*?)</span>',str(l_class))[0]
	except Exception, e:
		return {'price':'NA','url':l_link}	
	return {'price':l_price,'url':l_link}
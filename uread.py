import urllib2
from bs4 import BeautifulSoup
import pyisbn
import re
import time
import mechanize
def uread(isbn):
	if len(isbn) == 10:
		u_link = "http://www.uread.com/search-books/"+pyisbn.Isbn10(isbn).convert(code='978')
	else:
		u_link = "http://www.uread.com/search-books/"+isbn
	br = mechanize.Browser()
	#br.set_all_readonly(False)    # allow everything to be written to
	br.set_handle_robots(False)   # ignore robots
	br.set_handle_refresh(False)  # can sometimes hang without this
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]           # [('User-agent', 'Firefox')]
	try:
		response = br.open(u_link)
	except Exception, e:
		return {'price':'NA','url':u_link}
	u_soup = BeautifulSoup(response.read())
	u_tag = u_soup.select('#ctl00_phBody_ProductDetail_lblourPrice')
	if not u_tag:
		return {'price':'NA','url':u_link}
	else:
		u_tag = u_tag[0]
	try:
		u_price = re.findall(r'</span>(.*?)</label>',str(u_tag))[0]
	except Exception, e:
		return {'price':'NA','url':u_link}
	return {'price':u_price,'url':u_link}
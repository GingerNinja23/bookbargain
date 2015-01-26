import contextlib
import selenium.webdriver as webdriver
import bs4 as bs
import pyisbn
import re

def paytm(isbn):
	if len(isbn) == 10:
		p_link = 'https://paytm.com/shop/search/?q='+pyisbn.Isbn10(isbn).convert(code='978')+'&sort_price=1'
	else:		
		p_link = 'https://paytm.com/shop/search/?q='+isbn+'&sort_price=1'
	with contextlib.closing(webdriver.Firefox()) as driver:
	    try:
	    	driver.get(p_link)
	    	content = driver.page_source
	    	# print content
	    except Exception, e:
	    	print 'error'
	    	return 'NA'
	    	driver.quit()
	    	content = ''
	    soup = bs.BeautifulSoup(content)
	    p_class = soup.findAll('span',class_="border-radius ng-binding")
	    # print p_class
	    if not p_class:
	    	return 'NA'
	    else:
	    	p_class = p_class[0]
	    	p_price = re.findall(r'>Rs (.*?)</span>',str(p_class))[0]
	    	return p_price
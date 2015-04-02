import selenium.webdriver as webdriver
import bs4 as bs
import pyisbn
import re

def paytm(isbn):
	if len(isbn) == 10:
		p_link = 'https://paytm.com/shop/search/?q='+pyisbn.Isbn10(isbn).convert(code='978')+'&sort_price=1'
	else:		
		p_link = 'https://paytm.com/shop/search/?q='+isbn+'&sort_price=1'
	# print p_link
	driver = webdriver.PhantomJS('phantomjs',service_args=['--ssl-protocol=any'])
	# driver = webdriver.Firefox()
	try:
		driver.get(p_link)
		content = driver.page_source
	except:
		content = ''
		return {'price':'NA','url':p_link}
	# print content	
	driver.quit()
	soup = bs.BeautifulSoup(content)
	p_class = soup.findAll('span',class_="border-radius ng-binding")
	# print p_class
	if not p_class:
		return {'price':'NA','url':p_link}	
	else:
		p_class = p_class[0]
	try:
		p_price = re.findall(r'>Rs (.*?)</span>',str(p_class))[0]
		return {'price':p_price,'url':p_link}
	except Exception, e:
		return {'price':'NA','url':p_link}
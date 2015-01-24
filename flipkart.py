import urllib2
from bs4 import BeautifulSoup
import time
import mechanize
import re


def flipkart(isbn):
	#Getting the Source
	start_time = time.time()
	f_link = "http://www.flipkart.com/search?q="+isbn
	br = mechanize.Browser()
	br.set_handle_robots(False)   # ignore robots
	br.set_handle_refresh(False)  # can sometimes hang without this
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]# [('User-agent', 'Firefox')]
	response = br.open(f_link)

	#Creating the soup

	f_soup = BeautifulSoup(response.read())

	#Getting the data
	f_title_temp =(f_soup.find(itemprop="name"))
	if(f_title_temp):
		f_title = f_title_temp.string

		f_price_temp = f_soup.find_all("span",class_="selling-price omniture-field")[0]
		if(f_price_temp):
			f_price=(f_price_temp.string).replace('Rs. ','')
		else:
			f_price="NA"

		f_author_temp = (f_soup.find_all(href=re.compile("/author/[\w\s,.$><?@#$%^&*()_:-]+"))[0])
		if(f_author_temp):
			f_author = f_author_temp.string
		else:
			f_author="NA"

		f_img_temp = (f_soup.find_all("img",class_="productImage  current")[0])['data-src']
		if(f_img_temp):
			f_img=f_img_temp
		else:
			f_img = "NA"

	else:
		f_title = "NA"
		f_price="NA"
		f_author="NA"
		f_img = "NA"

	print time.time()-start_time
	flip_dict = {'name':f_title,'price':f_price,'author':f_author,'image_url':f_img}

	return flip_dict


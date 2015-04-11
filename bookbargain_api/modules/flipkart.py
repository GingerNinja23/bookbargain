import urllib2
from bs4 import BeautifulSoup
import mechanize
import re
import pyisbn

def flipkart(isbn):

	# Getting the Source from the link

	if len(isbn) == 10:
		f_link = "http://www.flipkart.com/search?q="+pyisbn.Isbn10(isbn).convert(code='978')
	else:
		f_link = "http://www.flipkart.com/search?q="+isbn
		
	f_link = f_link +"&affid=sriteja96" # Affliate ID
	br = mechanize.Browser()
	br.set_handle_robots(False)   # Ignore robots.txt
	br.set_handle_refresh(False)  
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

	try:
		response = br.open(f_link)

	except Exception, e:
		f_title = "NA"
		f_price = "NA"
		f_author = "NA"
		f_img = "NA"
		f_desc = "NA"
		f_status = "error_connecting"
		flip_dict = {'name':f_title,'price':f_price,'author':f_author,'image_url':f_img,'desc':f_desc,'url':f_link, 'status':f_status}
		return flip_dict

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

		f_desc_temp = f_soup.find_all("div",class_="description-text")

		if(f_desc_temp):
			f_desc = f_desc_temp[0].decode_contents(formatter="html")
			soup = BeautifulSoup(f_desc)
			f_desc = soup.get_text()
		else:
			f_desc="NA"

		f_status = "success"

	else:
		f_title = "NA"
		f_price = "NA"
		f_author = "NA"
		f_img = "NA"
		f_desc = "NA"
		f_status =  "invalid_isbn"

	flip_dict = {'name':f_title,'price':f_price,'author':f_author,'image_url':f_img,'desc':f_desc,'url':f_link,'status':f_status}

	return flip_dict



import urllib2
from bs4 import BeautifulSoup
import time
import mechanize


start_time = time.time()
f_link = "http://www.flipkart.com/search?q=9789380501932"
#f_soup = BeautifulSoup((urllib2.urlopen(f_link)).read())
#print f_soup.prettify()
#f_temp =(f_soup.find_all(itemprop='price'))
#print f_temp
# if (f_temp):
#     f_temp=f_temp[0]
#     booknametemp=f_soup.find(itemprop="name")
#     bookname=re.search('>[\w\s,.$><?@#$%^&*()_:-]+<',str(booknametemp)).group(0)[1:-1]
#     author= BeautifulSoup(str(f_soup.find_all(href=re.compile("/author/[\w\s,.$><?@#$%^&*()_:-]+"))[0])).find('a').getText()
#     f_price = BeautifulSoup(str(f_temp)).meta['content']
#     f_availtemp=f_soup.select(".instock")
#     if(f_availtemp):
#         f_avail="Available"
#     else:
#         f_avail="Out Of Stock"
#     img_temp = f_soup.select(".product-image ")
#     if(not img_temp):
# 	    imgurl = BeautifulSoup(str(f_soup.find(id="mprodimg-id"))).img['data-src']
#     else:
# 	    imgurl = BeautifulSoup(str(img_temp[0])).img['src']
# else:
#     f_price="NA"
#     f_avail="NA"
#     imgurl=""
#     bookname=""
#     author=""
#     fflag=True
# flist = [f_price,f_avail,f_link,imgurl,bookname,author,fflag]
# print "flipkart finished"
# return flist


br = mechanize.Browser()
#br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]           # [('User-agent', 'Firefox')]
response = br.open(f_link)
#print response.read()      # the text of the page
response1 = br.response()  # get the response again#
#print response1.read()     # can
print time.time()-start_time
f_soup = BeautifulSoup(response.read())
#print f_soup.prettify()
f_temp =(f_soup.find_all(itemprop='price'))
print f_temp

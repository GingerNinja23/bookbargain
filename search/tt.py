from bs4 import BeautifulSoup
import urllib
import re
def flipkart(isbn):
#Flipkart Price Fetch
    f_link = "http://www.flipkart.com/search?q="+isbn
    f_soup = BeautifulSoup((urllib.urlopen(f_link)).read())
    f_temp =(f_soup.find_all(itemprop='price'))
    if (f_temp):
        f_temp=f_temp[0]
        booknametemp=f_soup.find(itemprop="name")
        bookname=re.search('>[\w\s,.$><?@#$%^&*()_:-]+<',str(booknametemp)).group(0)[1:-1]
        author= BeautifulSoup(str(f_soup.find_all(href=re.compile("/author/[\w\s,.$><?@#$%^&*()_:-]+"))[0])).find('a').getText()
        f_price = BeautifulSoup(str(f_temp)).meta['content']
        f_availtemp=f_soup.select(".instock")
        if(f_availtemp):
            f_avail="Available"
        else:
            f_avail="Out Of Stock"
        img_temp = f_soup.select(".product-image ")
        if(not img_temp):
    	    imgurl = BeautifulSoup(str(f_soup.find(id="mprodimg-id"))).img['data-src']
        else:
    	    imgurl = BeautifulSoup(str(img_temp[0])).img['src']
    else:
        f_price="NA"
        f_avail="NA"
        imgurl=""
        bookname=""
        author=""
        fflag=True
    flist = [f_price,f_avail,f_link,imgurl,bookname,author]
    return flist

    
flist = flipkart("9781409081524")
print flist



    
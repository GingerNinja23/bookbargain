import urllib2
from bs4 import BeautifulSoup
import pyisbn
import re
import time
import mechanize
isbn = '9789380501932'
i_link = "http://www.infibeam.com/Books/search?q="+isbn
br = mechanize.Browser()
#br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]           # [('User-agent', 'Firefox')]
response = br.open(i_link)
i_soup = BeautifulSoup(response.read())
i_class = i_soup.findAll('span',class_='final-price')
i_price = re.findall(r'</span> (.*?)</span>',str(i_class))[0]
print i_price
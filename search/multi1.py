
from bs4 import BeautifulSoup
import urllib2
import re
from amazon import  amazon
from bookadda import bookadda
from infibeam import infibeam
from flipkart import flipkart
from indiatimes import indiatimes
from homeshop18 import hs18
from threading import Thread
from time import sleep
import time
from multiprocessing.pool import ThreadPool


start_time = time.time()
isbn=str(9780307474278)
pool = ThreadPool(processes=6)
async_result1 = pool.apply_async(amazon, (isbn,))
async_result2 = pool.apply_async(bookadda, (isbn,))
async_result3 = pool.apply_async(infibeam, (isbn,))
async_result4 = pool.apply_async(indiatimes, (isbn,))
async_result5 = pool.apply_async(hs18, (isbn,))
async_result6 = pool.apply_async(flipkart, (isbn,))

alist = async_result1.get()
blist = async_result2.get()
iblist = async_result3.get()
itlist = async_result4.get()
hlist = async_result5.get()
flist = async_result6.get()
print time.time() - start_time, "seconds"

print alist,blist,iblist,itlist,hlist,flist
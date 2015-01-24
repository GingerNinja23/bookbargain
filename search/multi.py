
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
import Queue

queue=Queue.Queue()
isbn=str(9789351362258)
thread1= Thread(target = amazon, args=[isbn,queue])
thread2= Thread(target = bookadda, args=[isbn,queue])
thread3= Thread(target = infibeam, args=[isbn,queue])
#thread4= Thread(target = amazon, args=[isbn])
#thread5= Thread(target = amazon, args=[isbn])
#thread6= Thread(target = amazon, args=[isbn])

thread1.start()
thread2.start()
thread3.start()
jo()
def jo():
	thread1.join()
	thread2.join()
	thread3.join()
print queue
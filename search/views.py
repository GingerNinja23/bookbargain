from django.shortcuts import render
from django.shortcuts import render_to_response
from  django.template import RequestContext
from bs4 import BeautifulSoup
import urllib2
import re
from multiprocessing.pool import ThreadPool
import pyisbn
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

# Create your views here.
def isbn(request):
        return render_to_response('isbn.html',RequestContext(request))


def search_isbn(request):
	if request.method == 'POST':
		isbn=str(request.POST.get('isbn'))
		if(pyisbn.validate(isbn)):
		    pool=ThreadPool(processes=6)
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
		    a_price=alist[0]
		    a_avail=alist[1]
		    a_link =alist[2]
		    b_price =blist[0]
		    b_avail=blist[1]
		    b_link=blist[2]
		    ib_price=iblist[0]
		    ib_avail=iblist[1]
		    ib_link=iblist[2]
		    it_price=itlist[0]
		    it_avail=itlist[1]
		    it_link=itlist[2]
		    h_price=hlist[0]
		    h_avail=hlist[1]
		    h_link = hlist[2]
		    f_price=flist[0]
		    f_avail=flist[1]
		    f_link = flist[2]
		    imgurl=flist[3]
		    bookname=flist[4]
		    author=flist[5]
		    fflag=flist[6]
		    if(fflag):
		        return render(request,'isbn.html',{"message":"No Data Found/Given ISBN is an e-book"})
		    else:
		        return render(request,'results.html',{'a_price': a_price,'b_price': b_price,'ib_price': ib_price,'it_price': it_price,'h_price': h_price,'f_price': f_price,"imgurl":imgurl,'a_link': a_link,'b_link': b_link,'it_link': it_link,'ib_link': ib_link,'h_link': h_link,'f_link': f_link,'a_avail': a_avail,'b_avail': b_avail,'ib_avail': ib_avail,'it_avail': it_avail,'h_avail': h_avail,'f_avail': f_avail,"bookname":bookname,"author":author})
		else:
		    return render(request,'isbn.html',{"message":"Please enter a valid ISBN -13 number."})



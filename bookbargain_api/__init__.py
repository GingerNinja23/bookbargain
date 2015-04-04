from flask import Flask, request, jsonify
import multiprocessing.pool as mpool

from .modules.flipkart import flipkart
from .modules.amazon import amazon
from .modules.uread import uread
from .modules.crossword import crossword
from .modules.landmark import landmark
from .modules.infibeam import infibeam

from collections import OrderedDict

import json

app = Flask(__name__)

def worker((target, isbn)):
    return target(isbn)

@app.route("/api",methods=['GET'])
def api():
	pool = mpool.ThreadPool()
	isbn = request.args.get('isbn')
	args = [(target, isbn) for target in (flipkart,amazon,uread,crossword,landmark,infibeam)]
	result = pool.map(worker, args)


	data = OrderedDict()
	if(result[0]['name]!="NA"):
		data["Status"]="Success"
		data["Book Name"]=result[0]['name']
		data["Author"]=result[0]['author']
		data["Description"]=result[0]['desc']
		data["Image"]=result[0]['image_url']
		data["Flipkart Price"]=result[0]['price']
		data["Flipkart URL"]=result[0]['url']
		data["Amazon Price"]=result[1]['price']
		data["Amazon URL"]=result[1]['url']
		data["URead Price"]=result[2]['price']
		data["URead URL"]=result[2]['url']
		data["Crossword Price"]=result[3]['price']
		data["Crossword URL"]=result[3]['url']
		data["Landmark on the net Price"]=result[4]['price']
		data["Landmark on the net URL"]=result[4]['url']
		data["Infibeam Price"]=result[5]['price']
		data["Infibeam URL"]=result[5]['url']
	else:
		data["Status"]="Failed/Incorrect ISBN"
	return json.dumps(data)

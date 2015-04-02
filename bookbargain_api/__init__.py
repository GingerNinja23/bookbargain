from flask import Flask, request
import multiprocessing.pool as mpool

from .modules import flipkart,amazon,uread,crossword,landmark,infibeam
app = Flask(__name__)

def worker(target, isbn):
    return target(isbn)

@app.route("/api")
def api():
	pool = mpool.ThreadPool()
	isbn = int(request.args.get('isbn'))
	args = [(target, isbn) for target in (flipkart,amazon,uread,crossword,landmark,infibeam)]
	result = pool.map(worker, args)
	flip = result[0]
	return flip['name']
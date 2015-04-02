from flask import Flask, request
import multiprocessing.pool as mpool

from .modules.flipkart import flipkart
from .modules.amazon import amazon
from .modules.uread import uread
from .modules.crossword import crossword
from .modules.landmark import landmark
from .modules.infibeam import infibeam

app = Flask(__name__)

def worker((target, isbn)):
    return target(isbn)

@app.route("/api")
def api():
	pool = mpool.ThreadPool()
	isbn = request.args.get('isbn')
	args = [(target, isbn) for target in (flipkart,amazon,uread,crossword,landmark,infibeam)]
	result = pool.map(worker, args)
	flip = result[0]
	return flip['name']
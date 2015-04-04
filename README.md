# Bookbargain API Server
An open source RESTful API, that delivers the information of a book and its prices from various Indian E-Commerce stores. The API takes ISBN 10/13 as the input.

###Currently supported stores:

* Flipkart
* Amazon(India)
* Infibeam
* uRead
* Crossword
* Landmark on the net

###Usage

Users are encouraged to setup their own server. But for a small number of requests, users can use our server.<br><br>
The usage of the server is as follows:
```
http://bookbargain.in/api?isbn=[ISBN number 10/13]
                    (OR)
http://[ip-address-of-your-own-server]/api?isbn=[ISBN number 10/13]                    
```
For example, if you want to get the information of a book with ISBN number 9780007282548, your request would be similar to
```
http://bookbargain.in/api?isbn=9780007282548
```
This call would return a JSON object, containing all the information and prices of the book.


### Setting up your own server

The server is implemented using Flask. So you need to have Python and pip installed.<br>

These instructions are for Ubuntu/Debian Wheezy


##### Installing pip:

Python 2.7.9 and later have pip installed by default. You can skip this step if you already have pip installed.
```
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
```

##### Installing dependencies:

It is recommended to use virtualenv for setting up the server <br>

```
sudo pip install virtualenv
virtualenv env
.env/bin/activate
sudo pip install flask,pyisbn,mechanize,BeautifulSoup4
```
##### Downloading the source:
``` 
wget http://goo.gl/A6wdf7
tar xvzf bookbargain-api-server-v0.9.1-beta.tar.gz
cd bookbargain-api-server-v0.9.1-beta
```

##### Running the server:

```
python runserver.py
````

Running this command will start the server which by default, listens on all interfaces on port 80. The port number can be easily changed by modifying the following line in runserver.py

```
app.run(host='0.0.0.0',port=80,debug=False)
```


### Issues

If you encounter any issue/bug, please submit an issue on the project issue page or shoot me a mail.
For any other queries/feature-request, please contact me via email.

### Abuse

It's possible for someone to DDoS our server by writing a client that abuses the API. Doing so would force us to bring down our server, which would cause a lot of trouble for the users using our server for API requests. So we kindly request you to avoid such activities. _Please don't be evil!_




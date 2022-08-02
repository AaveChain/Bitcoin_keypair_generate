import os
from flask import Flask, request



app = Flask(__name__)


@app.route('/home')  
def home():  
    return "hello, welcome to our website";  

#@app.route('/generateKey', methods=['GET'])
#def generateKey():
 #   return "generateKey.py"

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
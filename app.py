"""
    create flask app for Caesar & Vigenere ciphers and their cryptanalysis using GA (Genetic Algorithm)
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: Dec. 1st, 2018
"""

from flask import Flask, request, render_template
import caesar_cipher
import vigenere_cipher

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/caesar_shift', methods=['GET', 'POST'])
def caesar_shift():
    return render_template("caesar_shift.html")

@app.route('/vigenere_cipher', methods=['GET', 'POST'])
def vigenere_cipher():
    return render_template("vigenere_cipher.html")
    
if __name__ == '__main__':
	app.run(debug = True)  
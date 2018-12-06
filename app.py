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

@app.route('/caesar', methods=['GET', 'POST'])
def caesar():
    if request.method == 'POST':
        plain_text = request.form['plain_text']
        cipher_text = request.form['cipher_text']
        function = request.form.get('choices')
        key_size = int(request.form.get('key_choices'))
        print(plain_text, cipher_text, function)
        if str(function) == "Encrypt":
            return render_template('caesar.html', data=[25, plain_text, caesar_cipher.encrypt(plain_text, key_size)])
        if str(function) == "Decrypt":
            return render_template('caesar.html', data=[25, caesar_cipher.decrypt(cipher_text, key_size), cipher_text])
        if str(function) == "Crack":
            print(caesar_cipher.crack(cipher_text)[0])
            return render_template('caesar.html', data=[25, caesar_cipher.crack(cipher_text), cipher_text])
    return render_template("caesar.html", data=[25, "Plain Text", "Cipher Text"])

@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    if request.method == 'POST':
        plain_text = request.form['plain_text']
        cipher_text = request.form['cipher_text']
        function = request.form.get('choices')
        keyword = str(request.form["keyword"])
        print(plain_text, cipher_text, function)
        if str(function) == "Encrypt":
            return render_template('vigenere.html', data=[plain_text, vigenere_cipher.encrypt(plain_text, keyword)])
        if str(function) == "Decrypt":
            return render_template('vigenere.html', data=[vigenere_cipher.decrypt(cipher_text, keyword), cipher_text])
    #     if str(function) == "Crack":
    #         print(caesar_cipher.crack(cipher_text)[0])
    #         return render_template('caesar.html', data=[caesar_cipher.crack(cipher_text), cipher_text])
    return render_template("vigenere.html", data=["Plain Text", "Cipher Text"])

    
if __name__ == '__main__':
	app.run(debug = True)  
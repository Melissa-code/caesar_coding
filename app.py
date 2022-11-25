from flask import Flask, render_template, request, session

app = Flask(__name__)

passwordApp = "123soleil"

app.secret_key = "azertyuiop"


@app.route('/')
def home():
    global passwordApp
    if 'pwd' in session:
        if session['pwd'] == passwordApp:
            return render_template('home.html')
        else:
            return render_template('safe.html')
    else:
        return render_template('safe.html')


@app.route('/passwordValidation', methods=['POST'])
def passwordValidation():
    global passwordApp
    password = request.form['password']
    session['pwd'] = password
    if passwordApp == password:
        return render_template('home.html')
    else:
        return render_template('safe.html')


@app.route('/logout')
def logout():
    session.pop('pwd', None)
    return render_template('safe.html')


@app.route('/codage', methods=['POST'])
def coding():
    messageNoncode = request.form['message']
    decalageCode = request.form['decalageCode']
    messageCode = ""

    for lettreNonCodeeDeTypeTexte in messageNoncode:
        lettreNonCodeeDeTypeTexte = ord(lettreNonCodeeDeTypeTexte)
        lettreCodeeDeTypeUnicode = lettreNonCodeeDeTypeTexte + int(decalageCode)
        lettreCodeeDeTypeTexte = chr(lettreCodeeDeTypeUnicode)
        messageCode = messageCode + lettreCodeeDeTypeTexte

    return render_template('codingCaesar.html', messageNonCodeHtml=messageNoncode, messageCodeHtml=messageCode)


@app.route('/decodage', methods=['POST'])
def decoding():
    messageCode = request.form['messageCode']
    decalageDecode = request.form['decalageDecode']
    messageDecode = ""

    for lettreCodeeDeTypeTexte in messageCode:
        lettreCodeeDeTypeUnicode = ord(lettreCodeeDeTypeTexte)
        lettreDecodeeDeTypeUnicode = lettreCodeeDeTypeUnicode - int(decalageDecode)
        lettreDecodeeDeTypeTexte = chr(lettreDecodeeDeTypeUnicode)
        messageDecode = messageDecode + lettreDecodeeDeTypeTexte

    return render_template('decodingCaesar.html', messageCodeHtml=messageCode, messageDecodeHtml=messageDecode)


if __name__ == '__main__':
    app.debug = True
    app.run()

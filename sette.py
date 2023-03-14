from flask import Flask, render_template
app = Flask(__name__)

import datetime
def controllo():
    orario = int(datetime.datetime.now().time().hour)
    if orario <= 12:
        colore = "lightblue"
    elif orario > 12 and orario < 20:
        colore = "Yellow"
    else:
        colore = "Blue"
    return colore

@app.route('/', methods=['GET'])
def home():
    return render_template('tour7.html', sfondo = controllo())

@app.route('/paginacosti/<costo>', methods=['GET'])
def costovisita(costo):
    return render_template('paginacosti.html', prezzo = costo)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
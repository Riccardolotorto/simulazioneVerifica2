from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('tour6.html')

@app.route('/paginacosti/<costo>', methods=['GET'])
def costovisita(costo):
    return render_template('paginacosti.html', prezzo = costo)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
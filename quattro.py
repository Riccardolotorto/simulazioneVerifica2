from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('tour4.html')

@app.route('/visitasingola', methods=['GET'])
def visitasingola():
    return render_template('visitasingola.html')

@app.route('/visitagruppo', methods=['GET'])
def visitagruppo():
    return render_template('visitagruppo.html')

@app.route('/visitaguidata', methods=['GET'])
def visitaguidata():
    return render_template('visitaguidata.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/immagini', methods=['GET'])
def immagini():
    return render_template('immagini.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
    
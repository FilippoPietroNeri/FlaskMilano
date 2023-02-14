#	Esercizio 1:
#	Realizzare un sito web con flask che offra le seguenti funzionalità:
# 	
#	1. La homepage deve fornire una breve descrizione delle caratteristiche della città di Milano.
#	2. Al link <homesito>/immagini devono essere visualizzate le immagini di 4 monumenti di Milano 
#		(Controllare sul sito del prof) come si fa a mettere le immagini. https://github.com/wtitze/flask
#	3. Fare in modo che cliccando su un immagine si venga mandati ad un breve testo descrittivo di un monumento
#		(Controllare sul sito del prof) su come si fa.
#	4. La repository che conterrà il sito, si chiamerà FlaskMilano 

from flask import Flask,render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/immagini', methods=['GET'])
def immagini():
    return render_template('immagini.html')

# Monumenti #
@app.route('/monumenti/arcodellapace')
def arcodellapace():
    return render_template('/monumenti/arcodellapace.html')

@app.route('/monumenti/leonardodavinci')
def leonardodavinci():
    return render_template('/monumenti/leonardodavinci.html')

@app.route('/monumenti/monumentoleonardo')
def monumentoleonardo():
    return render_template('/monumenti/monumentoleonardo.html')

@app.route('/monumenti/vittorioemanuele')
def vittorioemanuele():
    return render_template('/monumenti/vittorioemanuele.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
    
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def hello(name):
    return f"Hi {name}!"


@app.route('/repeat/<int:count>/<word>')
def repeat(word, count):
    repeated_word = (word + "<br>" + "</br>") * count 
    return repeated_word

# SENSEI BONUS
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."



if __name__=='__main__':
    
    app.run(debug=True)
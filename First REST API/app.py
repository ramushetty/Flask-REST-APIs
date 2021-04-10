from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Welcome to the first flask application"
@app.route('/user/<name>')
def user(name):
 return '<h1>Hello, {}!</h1>'.format(name)



app.run(port=5000)


app.run(debug=True)



<string:name> , <int:id> 
from flask import Flask

# once flask has been imported an instance of the flask app must be instantiated
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Home Page</h1>'

if __name__ == '__main__':
    app.run(debug=True)
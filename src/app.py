from flask import Flask, render_template, request, send_from_directory
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# once flask has been imported an instance of the flask app must be instantiated
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'static/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for upload in request.files.getlist("file"):
        print(upload)
        filename = upload.filename
        destination = "/".join([target, filename])
        print(destination)
        upload.save(destination)

    return render_template('show.html', filename=filename)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("static", filename)

if __name__ == '__main__':
    app.run(debug=True)
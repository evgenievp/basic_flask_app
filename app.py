from flask import Flask, render_template

app = Flask(__name__)


json = 'https://api.npoint.io/fb1e14cf68a182ab0d9a'


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=False)
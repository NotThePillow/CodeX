from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/devs')
def test():
    return render_template('devs.html')

@app.route('/credits.txt')
def text():
    return credits

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

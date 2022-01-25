import sys
import subprocess
import pkg_resources

required = {'flask'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
print("checking files")

from flask import Flask,render_template
try: 
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
except:
    pass
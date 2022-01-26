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
    def dark():
        return render_template()

    @app.route('/light')
    def light():
        return render_template('main_light.html')


    @app.route('/dark')
    def dark():
        return render_template('main_black.html')

except Exception:
    pass

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
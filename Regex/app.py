from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def regex_func():
    if request.method == 'POST':
        test_string = request.form['test_string']
        regex = request.form['regex']
        matches = re.findall(regex, test_string)
        return render_template('form.html', matches = matches)
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug = True)
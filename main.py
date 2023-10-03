from flask import Flask, render_template, request
import VADER_

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    text = None
    if request.method == 'POST':
        _text = request.form['commint']
        text = VADER_.sentiment(_text)
    return render_template('index.html', title='Home', text=text)

if __name__ == '__main__':
    app.run(debug=True, port=1234)

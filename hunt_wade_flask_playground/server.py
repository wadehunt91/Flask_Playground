from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def main():
    return render_template('index.html', num = 3, color = 'blue')

@app.route('/play/<int:num>')
def two(num):
    return render_template('index.html', color='blue', num = num)

@app.route('/play/<int:num>/<string:color>')
def three(num, color):
    return render_template('index.html', color=color, num = num)

if __name__=="__main__":
    app.run(debug=True)
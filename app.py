from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('ht1.html')
@app.route('/welcome/<username>')
def welcome(username):
    return f"Welcome, {username}!"
@app.route('/welcome/<id>')
def id_on(id):
    return f"Your Id is,{id}."
@app.route('/welcome/<pos>')
def position(pos):
    return f"Your position is,{pos}."
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['username']
    return redirect(url_for('welcome', username=name))
if __name__ == '__main__':
    app.run(debug=True)

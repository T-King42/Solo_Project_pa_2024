from flask_app import app
from flask import Flask,render_template

@app.route('/')
def log():
    return render_template('log_and_reg.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@app.route('/new_deck')
def new_deck():
    return render_template('new_deck.html')
@app.route('/edit_deck')
def edit_deck():
    return render_template('edit_deck.html')
@app.route('/card_view')
def card_view():
    return render_template('card_view.html')


if __name__==('__main__'):
    app.run(debug=True)
from flask_app import app
from flask import request,render_template,redirect
from flask_app.models.card import Card
from flask_app.models.card_in_deck import Card_in_deck
from flask_app.models.deck import Deck

@app.route('/card_view')
def card_view():
    return render_template('card_view.html')

@app.route('/test',methods=['GET'])
def test():
    Card.add_single_card('Raigeki')
    return redirect('/home')
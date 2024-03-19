from flask_app import app
from flask import request,render_template,redirect
from flask_app.models.card import Card
from flask_app.models.card_in_deck import Card_in_deck
from flask_app.models.deck import Deck

@app.route('/card_view')
def card_view():
    return render_template('card_view.html')

@app.route('/add_card',methods=['POST'])
def new_card():
    name = request.form['card_name']
    data = {
        'id':request.form['deck_id']
    }
    deck = Deck.get_deck_by_id(data)
    Card.add_single_card(name)
    return redirect(f'/new_deck/{deck.id}')
    
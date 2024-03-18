from flask_app import app
from flask import request,render_template,redirect
from flask_app.models.card import Card
from flask_app.models.card_in_deck import Card_in_deck
from flask_app.models.deck import Deck

@app.route('/card_view')
def card_view():
    return render_template('card_view.html')
@app.route('/add_cards',methods=['POST'])
def add_cards():
    data = {
        'deck_id':request.form['deck_id'],
        'card_id':request.form['card_id'],
        'quantity':request.form['quantity']
    }
    deck_data={
        'id':request.form['deck_id']
    }
    deck = Deck.get_deck_by_id(deck_data)
    Card_in_deck.add_card_to_deck(data)
    return redirect(f'/new_deck/{deck.id}')

@app.route('/test',methods=['GET'])
def test():
    Card.add_single_card('Raigeki')
    return redirect('/home')
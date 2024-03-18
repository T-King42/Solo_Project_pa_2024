from flask_app import app
from flask import session,render_template,request,redirect
from flask_app.models.card import Card
from flask_app.models.deck import Deck
from flask_app.models.user import User

@app.route('/new_deck/<int:deck_id>')
def new_deck(deck_id):
    data = {
        'id':session['user_id']
    }
    deck_data ={
        'id':deck_id
    }
    all_cards = Card.get_all_cards()
    user = User.get_user_by_id(data)
    deck = Deck.get_deck_with_cards(deck_data)
    print(deck.cards_in_deck)
    return render_template('new_deck.html',user=user,deck=deck,all_cards=all_cards)
@app.route('/add_deck',methods=['POST'])
def add_deck():
    session['deck_name']=request.form['deck_name']
    if not Deck.validate_deck(request.form):
        print('Va;idation failed')
        return redirect('/dashboard')
    data = {
        'user_id':request.form['user_id'],
        'name':request.form['deck_name']
    }
    deck_id = Deck.add_deck(data)
    deck_data = {
        'id':deck_id
    }
    deck = Deck.get_deck_by_id(deck_data)
    return redirect(f'/new_deck/{deck.id}')
@app.route('/edit_deck')
def edit_deck():
    return render_template('edit_deck.html')
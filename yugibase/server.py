from flask_app import app
from flask import render_template,redirect,session
from flask_app.controllers import cards,decks,cards_in_decks,users
from flask_app.models.user import User
from flask_app.models.card import Card
from flask_app.models.deck import Deck

# home
@app.route('/')
def go_home():
    return redirect('/home')

@app.route('/home')
def home():
    top_cards = Card.top_cards()
    top_decks = Deck.top_decks()
    return render_template('home.html',top_decks=top_decks,top_cards=top_cards)

# dashboard
@app.route('/dashboard')
def dashboard():
    data ={
        'id':session['user_id']
    }
    user_data={
        'user_id':session['user_id']
    }
    user = User.get_user_by_id(data)
    user_decks = Deck.get_user_decks(user_data)
    fav_cards = Card.fav_cards()
    return render_template('dashboard.html',user=user,user_decks=user_decks,fav_cards=fav_cards)

if __name__==('__main__'):
    app.run(debug=True)
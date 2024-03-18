from flask_app import app
from flask import Flask,render_template,redirect,request,session,flash
from flask_bcrypt import bcrypt
from flask_app.models.user import User
from flask_app.models.card import Card
from flask_app.models.deck import Deck
from flask_app.models.card_in_deck import Card_in_deck

# Login
@app.route('/login_and_registration')
def log():
    return render_template('log_and_reg.html')
@app.route('/register',methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/login_and_registration')
    salt = bcrypt.gensalt()
    pw_hash = bcrypt.hashpw(request.form['password'].encode('utf-8'),salt)
    data = {
        'username':request.form['username'],
        'email':request.form['email'],
        'password':pw_hash
    }
    new_user = User.register(data)
    session['user_id'] = new_user
    session['is_logged'] = True
    return redirect('/dashboard')
@app.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    data = {
        'username': username,
        'password': password
    }

    user = User.login(data)

    if user:
        session['user_id'] = user.id
        session['is_logged'] = True
        return redirect('/dashboard')
    else:
        return redirect('/login_and_registration')
    
# home
@app.route('/')
def go_home():
    return redirect('/home')
@app.route('/home')
def home():
    top_cards = Card.top_cards()
    top_decks = Deck.top_decks()
    return render_template('home.html',top_decks=top_decks,top_cards=top_cards)
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login_and_registration')
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
# New Deck
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

# Edit Deck
@app.route('/edit_deck')
def edit_deck():
    return render_template('edit_deck.html')
# Card View
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
    Card.add_single_card('Ultimate Conductor Tyranno')
    return redirect('/home')


if __name__==('__main__'):
    app.run(debug=True)
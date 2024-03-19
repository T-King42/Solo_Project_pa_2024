from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.card import Card
from flask_app.models.deck import Deck

class Card_in_deck():
    def __init__(self,data):
        self.deck_id = data['deck_id']
        self.card_id = data['card_id']
        self.quantity = data['quantity']

    @classmethod
    def add_card_to_deck(cls,data):
        query = '''INSERT INTO decks_using_cards (deck_id,card_id,quantity)
                    VALUES (%(deck_id)s,%(card_id)s,%(quantity)s)'''
        result = connectToMySQL('yugibase_schema').query_db(query,data)
        return result
    @classmethod
    def delete_card_from_deck(cls,data):
        if int(data['quantity']) > 1:
            data['quantity'] = str(int(data['quantity']) - 1)
            query = '''UPDATE decks_using_cards
                        SET quantity = %(quantity)s
                        WHERE deck_id = %(deck_id)s AND card_id = %(card_id)s'''
            result = connectToMySQL('yugibase_schema').query_db(query,data)
            return result
        else:
            query = '''DELETE FROM decks_using_cards
                        WHERE deck_id = %(deck_id)s AND card_id = %(card_id)s'''
            result = connectToMySQL('yugibase_schema').query_db(query,data)
            return result
        
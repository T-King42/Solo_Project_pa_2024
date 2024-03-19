from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.card import Card
from flask import flash

class Deck:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.cards_in_deck = []
    @classmethod
    def add_deck(cls,data):
        query = '''INSERT INTO decks (user_id,name,created_at,updated_at)
                    VALUES (%(user_id)s,%(name)s,now(),now())'''
        result = connectToMySQL('yugibase_schema').query_db(query,data)
        return result
    @classmethod
    def get_user_decks(cls,data):
        query = '''SELECT * FROM decks
                    WHERE user_id = %(user_id)s'''
        result = connectToMySQL('yugibase_schema').query_db(query,data)
        decks = []
        for deck in result:
            new_deck = cls(deck)
            decks.append(new_deck)
        return decks    
    @classmethod
    def get_deck_by_id(cls,data):
        query = '''SELECT * FROM decks
                    WHERE id = %(id)s''' 
        results = connectToMySQL('yugibase_schema').query_db(query,data)
        if results:
            return cls(results[0])
        else:
            print('no user at ID')
            return None
    @classmethod
    def top_decks(cls):
        query = '''SELECT * FROM decks
                    ORDER BY id
                    LIMIT 10'''
        decks = []
        result = connectToMySQL('yugibase_schema').query_db(query)
        for deck in result:
            add_deck= cls(deck)
            decks.append(add_deck)
        return decks
    @classmethod
    def get_deck_with_cards(cls,data):
        query = '''SELECT * FROM decks
                    LEFT JOIN decks_using_cards ON decks.id = decks_using_cards.deck_id
                    LEFT JOIN cards ON decks_using_cards.card_id = cards.id
                    WHERE decks.id = %(id)s'''
        results = connectToMySQL('yugibase_schema').query_db(query,data)
        if results:
            deck_data = results[0]
            deck = cls(deck_data) 
            cards_in_deck = []
            for row in results:
                card_info = {
                    'id': row['card_id'],
                    'name': row['card_name'],
                    'atk': row['atk'],
                    'def': row['def'],
                    'effect': row['effect'],
                    'img': row['img'],
                    'quantity': row['quantity']
                }
                cards_in_deck.append(card_info)

                deck.cards_in_deck = cards_in_deck  
            return deck
        else:
            print('No deck found with the given ID')
            return None
    @classmethod
    def delete_deck(cls,data):
        query = '''DELETE FROM decks
                    WHERE id = %(id)s'''
        results = connectToMySQL('yugibase_schema').query_db(query,data)
        return results

    @staticmethod
    def validate_deck(deck):
        is_valid=True
        print(len(deck['deck_name']))
        if len(deck['deck_name']) < 2 or len(deck['deck_name']) > 20:
            flash('*Deck name is invalid', 'deck')
            is_valid = False
        return is_valid
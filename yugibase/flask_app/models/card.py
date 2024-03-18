from flask_app.config.mysqlconnection import connectToMySQL
import requests
import os

# Card Class
class Card:
    def __init__(self, data):
        self.id = data['id']
        self.card_name = data['card_name']
        self.atk = data.get('atk')
        self.defense = data.get('def')
        self.effect = data['effect']
        self.img = data['img']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
# Add a single card to database if one doesn't already exist 
    @classmethod
    def add_single_card(cls,data):
        # api call
        response = requests.get(f'https://db.ygoprodeck.com/api/v7/cardinfo.php?name={data}')
        # manage card data from api
        card_data = response.json()['data'][0]
        image_url = card_data['card_images'][0]['image_url']
        card_name = card_data['name']
        # This method was the bane of my existence. Saves Image to server.
        image_path = cls.save_image_locally(image_url,'card_images/',card_name)
        # Check if atk or def is None
        atk = card_data.get('atk', None)
        defense = card_data.get('def', None)
        # prep data for injection into database
        sql_data = {
            'card_name':card_data['name'],
            'atk':atk,
            'def':defense,
            'effect':card_data['desc'],
            'img':image_path
        }
        # save card
        cls.save_card(sql_data)
        return
    # SQL query for adding the card
    @classmethod
    def save_card(cls,data):
        query = '''INSERT into cards (card_name,atk,def,effect,img,created_at,updated_at)
                    VALUES (%(card_name)s,%(atk)s,%(def)s,%(effect)s,%(img)s,now(),now())'''
        result = connectToMySQL('yugibase_schema').query_db(query,data)
        return result
    # Brain melting section
    @staticmethod
    def save_image_locally(image_url, save_directory,card_name_json):
        # first the api image files are saved by ID not name. Gotta fix that
        card_name_no_spaces = card_name_json.replace(' ', '_')
        image_filename = f"{card_name_no_spaces}.jpg"
        # using new edited name, create a local file path
        image_path = os.path.join(save_directory, image_filename)
        # dont think this needs to be here after the first call, but makes it more portable I suppose
        os.makedirs(save_directory, exist_ok=True)
        # download the image
        response = requests.get(image_url)
        # check to see if download from server was successful
        if response.status_code == 200:
            with open(f'flask_app/static/'+ image_path, 'wb') as image_file:
                image_file.write(response.content)
            print('image written to file')
            print(image_path)
            # return path for insertion in DB
            return image_path
        else:
            print(f"Failed to download image from {image_url}. Status code: {response.status_code}")
            return None
    @classmethod
    def get_all_cards(cls):
        query = '''SELECT * FROM cards'''
        cards = []
        result = connectToMySQL('yugibase_schema').query_db(query)
        for card in result:
            new_card = cls(card)
            cards.append(new_card)
        return cards
    @classmethod
    def top_cards(cls):
        query = '''SELECT * FROM cards
                    ORDER BY id
                    LIMIT 5'''
        cards=[]
        result = connectToMySQL('yugibase_schema').query_db(query)
        for card in result:
            new_card = cls(card)
            cards.append(new_card)
        return cards
    @classmethod
    def fav_cards(cls):
        query = '''SELECT * FROM cards
                    ORDER BY id
                    LIMIT 4'''
        cards=[]
        result = connectToMySQL('yugibase_schema').query_db(query)
        for card in result:
            new_card = cls(card)
            cards.append(new_card)
        return cards
    # simple testing method I used to verify if card instance was created successfully 
    @staticmethod
    def print_card_data():
        print("Card Data:")
        for attribute, value in __dict__.items():
            print(f"{attribute}: {value}")
        return
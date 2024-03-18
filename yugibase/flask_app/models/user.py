from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.my_decks = []

    @classmethod
    def get_user_by_email(cls,data):
        query = '''SELECT * FROM users
                    WHERE email = %(email)s'''
        data = {
            'email':data
        }
        results = connectToMySQL('yugibase_schema').query_db(query,data)
        if results:
            return cls(results[0])
        else:
            flash('*invalid username or password','login')
            return None
    @classmethod
    def get_user_by_username(cls,data):
        query = '''SELECT * FROM users
                    WHERE username = %(username)s'''
        data = {
            'username':data
        }
        results = connectToMySQL('yugibase_schema').query_db(query,data)
        if results:
            return cls(results[0])
        else:
            flash('*invalid username or password','login')
            return None
    @classmethod
    def get_user_by_id(cls,data):
        query = '''SELECT * FROM users
                    WHERE id = %(id)s'''
        results = connectToMySQL('yugibase_schema').query_db(query,data)
        if results:
            return cls(results[0])
        else:
            return None
    @classmethod
    def register(cls,data):
        query = '''INSERT INTO users (username,email,password,created_at,updated_at)
                    VALUES (%(username)s,%(email)s,%(password)s,now(),now());'''
        results = connectToMySQL('yugibase_schema').query_db(query,data)
        return results
    @classmethod
    def login(cls,data):
        user = cls.get_user_by_username(data['username'])
        if user and bcrypt.checkpw(data['password'].encode('utf-8'),user.password.encode('utf-8')):
            return user
        else:
            flash('invalid username or password')
            return None
    @staticmethod
    def validate_user(user):
        is_valid = True
        if not user['username'] or not user['username'].isalpha() or len(user['username']) < 2:
            flash('*username is invalid.', 'register')
            is_valid = False
        else:
            existing_user = User.get_user_by_username(user['username'])
            if existing_user:
                flash('*username is taken.', 'register')
        if not user['email'] or not EMAIL_REGEX.match(user['email']):
            flash('*email is invalid', 'register')
            is_valid = False
        else:
            existing_user = User.get_user_by_email(user['email'])
            if existing_user:
                flash('*User already exists with this email.', 'register')
                is_valid = False
        if not user['password'] or len(user['password']) < 8 or user['password'] != user.get('confirm'):
            flash('*password is invalid.', 'register')
            is_valid = False

        return is_valid
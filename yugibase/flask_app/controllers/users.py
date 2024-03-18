from flask_app import app
from flask_app.models.user import User
from flask import request,session,redirect,render_template
from flask_bcrypt import bcrypt

@app.route('/login_and_registration')
def log():
    return render_template('log_and_reg.html')
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
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login_and_registration')
from flask import Flask, render_template, request, redirect, url_for, session
from flask.helpers import flash

app = Flask(__name__)
app.secret_key = b'\x8a\xf2N8\xd9\xa8\x06\xbc\x1b.\x87\xff\xa1S\x9f\xa6'

users = []

@app.route('/')
def index():
    return redirect(url_for('register'))

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        password = request.form.get('password')
        password_retry = request.form.get('password-retry')
        
        if password == password_retry:
            user = {
            'username': request.form.get('username'),
            'email': request.form.get('email'),
            'password': password
            }
            users.append(user)
            session['username'] = user['username']

            return redirect(url_for('cabinet'))
        else:
            flash('Passwords not equal!')
            return redirect(url_for('register'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        user = find_user(username)
        if user != None:
            if user['password'] == password:
                session['username'] = user['username']
                return redirect(url_for('cabinet'))
            else:
                return redirect(url_for('login'))
        else:
            return redirect(url_for('register'))

@app.route('/logout/', methods = ['GET'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/cabinet/', methods = ['GET'])
def cabinet():
    if 'username' in session:
        user = find_user(session['username'])
        return render_template('cabinet.html', user=user)
    else:
        return redirect(url_for('register'))

def find_user(username):
    return next((user for user in users if user["username"] == username), None)

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
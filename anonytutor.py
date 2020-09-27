from flask import Flask, render_template, redirect
from flask import request
from flask_bootstrap import Bootstrap
import pyrebase

config = {
    "apiKey": "AIzaSyBrJWvkCGl7VxQ-F2qBo1NnsFhsQeupGXE",
    "authDomain": "anonytutor-227e8.firebaseapp.com",
    "databaseURL": "https://anonytutor-227e8.firebaseio.com",
    "projectId": "anonytutor-227e8",
    "storageBucket": "anonytutor-227e8.appspot.com",
    "messagingSenderId": "297342048051",
    "appId": "1:297342048051:web:93ff4343557043cf369046",
    "measurementId": "G-JW6Q6JLX17",
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()

# db.child("Students").push({
#     'name': 'Shannon Brown',
#     'email': 'shannb2012@gmail.com',
#     'password': 'Shannon2'
#     })

user = db.child("Students").get()
user = dict(user.val()).values()
print(user)

app = Flask(__name__)

@app.route('/')
def profile():
    return render_template('home.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        email = request.form['email']
        password = request.form['password']
        for item in user:
            if email == item['email']:
                print("The email address is '" + email + "'")
                if password == item['password']:
                    print("The password is '" + password + "'")
                    return render_template('profile.html', name=item['name'])
    return redirect('/')

if __name__=="__main__":
    Bootstrap(app)
    app.run(debug=True)
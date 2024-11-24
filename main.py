from flask import Flask, render_template, request, jsonify, redirect, url_for
import pyrebase

app = Flask(__name__)

# Firebase Configuration
config = {
  "apiKey": "AIzaSyBmTfbl-jTJW28Co6BvWapaf99rAUF9SmA",
  "authDomain": "memo-project-e982f.firebaseapp.com",
  "projectId": "memo-project-e982f",
  "storageBucket": "memo-project-e982f.firebasestorage.app",
  "messagingSenderId": "855875391052",
  "appId": "1:855875391052:web:3de9a431c8288f2a4a6ee9",
  "measurementId": "G-4YGPNVDMFX",
  "databaseURL": "https://memo-project-e982f.firebaseio.com"  # Corrected
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# Home Route (Landing Page)
@app.route('/home')
def index():
    return render_template('index.html')
def get_user_info(user):
    return {
        "email" : user['email'],
    }
# Sign Up Route (Email and Password Sign Up)
@app.route('/signup', methods=['POST'])
def signup():
    # try:
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = auth.create_user_with_email_and_password(email, password)
        
        return render_template('interface.html', **get_user_info(user))
    # except Exception as e:
        # return render_template('error.html', error="This account already exists. Try logging in.")

# Sign In Route (Email and Password Sign In)
@app.route('/signin', methods=['POST'])
def signin():
    # try:
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = auth.sign_in_with_email_and_password(email, password)
        
        return render_template('interface.html', **get_user_info(user))
    # except Exception as e:
        # return render_template('error.html', error="No account found. Please sign up before logging in.")

if __name__ == '__main__':
    app.run(debug=True)

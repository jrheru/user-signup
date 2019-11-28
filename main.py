from flask import Flask, request, render_template, redirect
import jinja2
import os
import re
import html

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
# app.config['DEBUG'] = TRUE




@app.route('/')
def display_user_form():
    return render_template('index.html')

    
# def is_email(string):
#     atsign_index = string.find('@')
#     atsign_present = atsign_index >= 0
#     if not atsign_present:
#         return False
#     else:
#         domain_dot_index = string.find('.', atsign_index)
#         domain_dot_present = domain_dot_index  >= 0
#         return domain_dot_present

@app.route('/signup', methods=['POST'])
def validate_user():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error =''
    password_error =''
    verify_error = ''
    email_error = ''

    if username == '':
        username_error ='please enter a username'
    elif len(username) <= 3 or len(username) > 20:
        username_error = 'username length must be between 3 and 20 characters'
        username = ""
    elif " " in username:
        username_error = 'please enter a username without spaces'
        username = ""

    if password == '':
        password_error = 'please enter a password'
    elif len(password) <= 3 or len(password) > 20:
        password_error = 'password length must be between 3 and 20 characters'
    elif " " in password:
        password_error = 'password cannot contain spaces'

    if verify == '' or verify != password:
        verify_error = 'please verify password'
        verify = ""
    
    if email != "":
        
        if not re.match(r"(^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$)", email):
            email_error = 'This is not a vaild email, you can be left blank'
  
           
    if not username_error and not password_error and not verify_error and not email_error:
        username = username
        return render_template('welcome.html', username=username)
    
    
    else:
        return render_template('index.html',
        username = username,
        username_error = username_error,
        password = password,
        password_error = password_error,
        verify = verify,
        verify_error = verify_error,
        email = email,
        email_error = email_error)
        

app.route('/welcome')
def welcome_page():
    username =request.args.get('username')
    return render_template('welcome.html', username=username)
    



if __name__=='__main__':
    app.run(debug=True)


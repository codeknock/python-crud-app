from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
   #sending info to server
    data = request.form
    print(data)
    #info to server ended
    return render_template("login.html", boolean=True)
    
@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            #message flashing using flash by importing flash
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('firstName must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif  len(password1) < 7:
            flash('Password must be greater than 7 characters.', category='error')
        else:
            flash('Account created successfully!', category='success')
            
    return render_template("sign_up.html")
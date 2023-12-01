from flask import Blueprint,render_template, request, flash

#Setting up the BluePrint
auth = Blueprint('auth', __name__)

#Setting Routes

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout<p>"

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get(' password1')
        password2 = request.form.get(' password2')

        #Validation of credentials
        if len(email) < 4:
            flash('Email must have more than 4 Characters', category='error')
        elif len(firstName) < 2:
            flash('First name must have more than 1 character', category='error')
        elif password1 != password2:
            flash('Password do not match', category='error')
        elif len(password1) < 7:
            flash('Password must have more than 7 Characters', category='error')
        else:
            #Add the user to Database
            flash('Account Created Successfully!', category='success')
    return render_template("sign_up.html")

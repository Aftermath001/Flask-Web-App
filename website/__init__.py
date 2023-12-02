from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# Define and initialize DB
db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    # Encrypt and secure the cookies of our session data
    app.config['SECRET_KEY'] = 'mnbojklnods hiuhn'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    return app

def create_database(app):
    # Use path model to check if db exists
    db_path = path.join('website', DB_NAME)
    
    if not path.exists(db_path):
        # if not create db
        with app.app_context():
            db.create_all()
            print('Created Database!')

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)



# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# # from pathlib import Path
# from os import path
# #define and initialize DB
# db = SQLAlchemy()
# DB_NAME = 'database.db'


# def create_app():
#     app = Flask(__name__)
#     #Encrypt and secure the cookies of our session data
#     app.config['SECRET_KEY'] = 'mnbojklnods hiuhn'
#     app.config ['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
#     db.init_app(app)

#     from .views import views
#     from .auth import auth

#     app.register_blueprint(views, url_prefix='/')
#     app.register_blueprint(auth, url_prefix='/')

#     from .models import User, Note

#     create_database(app)

#     return app




# def create_database(app):
#     #Use path model to check if db exists
#     if not path.exists('website/' + DB_NAME):
#         #if not create db
#         db.create_all()
#         print('Created Database!')

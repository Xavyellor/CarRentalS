import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://<username>:<password>@<host>/<database_name>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable Flask-SQLAlchemy event system to save memory
    SECRET_KEY = 'your-secret-key'  # You can change this to something more secure

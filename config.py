from datetime import datetime, timedelta

SQLALCHEMY_DATABASE_URI = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SESSION_TYPE = 'filesystem'
PERMANENT_SESSION_LIFETIME = timedelta(days=1)
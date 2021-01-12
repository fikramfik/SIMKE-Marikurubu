from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask('__name__', template_folder='SIMKe/templates', static_folder='SIMKe/static')
app.config['SECRET_KEY']="fikramtamrin"
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///simke_marikurubu.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)

from SIMKe.user.routes import ruser
app.register_blueprint(ruser)

from SIMKe.admin.routes import radmin
app.register_blueprint(radmin)
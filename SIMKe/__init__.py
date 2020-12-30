from flask import Flask

app=Flask('__name__', template_folder='SIMKe/templates', static_folder='SIMKe/static')
app.config['SECRET_KEY']="fikramtamrin"

from SIMKe.user.routes import ruser
app.register_blueprint(ruser)

from SIMKe.admin.routes import radmin
app.register_blueprint(radmin)
from flask import render_template
from qa327 import app

#import routes
from qa327.views.home import home_page
from qa327.views.login import login_page
from qa327.views.logout import logout_page
from qa327.views.register import register_page
from qa327.views.buy import buy_page
from qa327.views.sell import sell_page
from qa327.views.update import update_page

"""
This file defines the front-end part of the service.
It links together the various route Blueprints that 
makeup this web-service and provides a catch all
error when an invalid route is met.
"""

#link routes
app.register_blueprint(home_page)
app.register_blueprint(login_page, url_prefix='/login')
app.register_blueprint(logout_page, url_prefix='/logout')
app.register_blueprint(register_page, url_prefix='/register')
app.register_blueprint(buy_page, url_prefix='/buy')
app.register_blueprint(sell_page, url_prefix='/sell')
app.register_blueprint(update_page, url_prefix='/update')

"""
display a catch all 404 error page whenever our app hits an unknown route.
"""
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='404'), 404

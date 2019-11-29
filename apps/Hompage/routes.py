from flask import Blueprint
from flask import render_template,g

Main_View = Blueprint('Main_View', __name__)

@Main_View.route('/homepage')
def home():
    template = "Home Page/Homepage.html"
    return render_template(template)


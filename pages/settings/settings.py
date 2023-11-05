from flask import Blueprint, render_template

settings = Blueprint('settings', __name__, template_folder='templates', static_folder='statics')

@settings.route('/')
def index():
    return render_template('settings.html')
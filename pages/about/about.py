from flask import Blueprint, render_template

about = Blueprint('about', __name__, template_folder='templates', static_folder='statics')

@about.route('/')
def index():
    return render_template('about.html')
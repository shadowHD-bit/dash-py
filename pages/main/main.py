from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='templates', static_folder='statics')

@main.route('/main')
def index():
    return render_template('main.html')
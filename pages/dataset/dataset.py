from flask import Blueprint, render_template
from dash_gh.dataset_dash import dataset_app

dataset = Blueprint('dataset', __name__, template_folder='templates', static_folder='statics')
dash_html = dataset_app.layout.to_html()

@dataset.route('/')
def index():
    return render_template('dataset.html', dash_html=dash_html)


from flask import Flask, render_template
from pages.main.main import main
from pages.about.about import about
from pages.settings.settings import settings

app = Flask(__name__, template_folder="partials", static_folder="statics")
app.register_blueprint(main, url_prefix="/")
app.register_blueprint(about, url_prefix="/about")
app.register_blueprint(settings, url_prefix="/settings")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
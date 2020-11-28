import os
from flask import Flask
from flask_cors import CORS
from src.util.helpers import load_file
from src.routers.basic import basic_flip, basic_grind, basic_manual
from src.routers.advanced import advanced_flip, advanced_grind, advanced_manual
from src.routers.insane import insane_flip, insane_grind, insane_manual

app = Flask(__name__)
CORS(app)

app.add_url_rule("/api/v1/basic/flip",   view_func=basic_flip)
app.add_url_rule("/api/v1/basic/grind",  view_func=basic_grind)
app.add_url_rule("/api/v1/basic/manual", view_func=basic_manual)

app.add_url_rule("/api/v1/insane/flip",   view_func=insane_flip)
app.add_url_rule("/api/v1/insane/grind",  view_func=insane_grind)
app.add_url_rule("/api/v1/insane/manual", view_func=insane_manual)

app.add_url_rule("/api/v1/advanced/flip",   view_func=advanced_flip)
app.add_url_rule("/api/v1/advanced/grind",  view_func=advanced_grind)
app.add_url_rule("/api/v1/advanced/manual", view_func=advanced_manual)


if __name__ == "__main__":
    if os.environ['USER'] == "pi":
        app.run(host="0.0.0.0", port=7000)
    else:
        app.run(debug=True)
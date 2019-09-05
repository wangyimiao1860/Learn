#-*-coding:utf-8 -*-
from flask import Flask


from concurrent.futures import ThreadPoolExecutor

# app = Flask(__name__)
# app.config["EXPLAIN_TEMPLATE_LOADING"] = True

# from .controller import view

# print(__name__)

def create_app():
    app = Flask(__name__)
    executor = ThreadPoolExecutor(3)
    from .controller import view
    app.register_blueprint(view.bp)
    return app

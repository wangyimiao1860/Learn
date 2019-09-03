#-*-coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)
app.config["EXPLAIN_TEMPLATE_LOADING"] = True

from .controller import view

print(__name__)

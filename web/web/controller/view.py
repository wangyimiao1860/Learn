

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from ..model.model import getStore, update_store

bp = Blueprint('index', __name__)


@bp.route('/', methods=['GET', 'POST'])
def home():
    
    return render_template("index.html")

@bp.route('/signin', methods=["GET",'POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.method == "GET":
        return render_template("login.html")
    else:
        print(request.form)
        if request.form['username']=='admin' and request.form['password']=='password':
            return '<h3>Hello, admin!</h3>  '
        return '<h3>Bad username or password.</h3>'@app.route('/show', methods=['GET'])

@bp.route('/show',methods=['GET'])
def show():
    store = getStore()
    return render_template("show.html",store=store)   
   
@bp.route('/go_buy',methods=['GET', "POST"])
def go_buy():
    if request.method == "GET":
        fruit = request.args.get("fruit")
        return render_template("go_buy.html" , fruit=fruit)
    else:
        fruit = request.form.get("fruit")
        num = int(request.form.get("num"))
        update_store(fruit, num)
        return render_template("go_buy.html")


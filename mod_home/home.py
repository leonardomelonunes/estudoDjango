#coding: utf-8
from flask import Blueprint, render_template, request
from mod_login.login import validaSessao

bp_home = Blueprint('home', __name__, url_prefix='/home', template_folder='templates')

@bp_home.route("/", methods=['GET', 'POST'])
@validaSessao
def home():
    return render_template("home.html")

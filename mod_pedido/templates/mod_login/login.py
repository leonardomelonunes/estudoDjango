#coding: utf-8
from flask import Blueprint, render_template, request, request, redirect, url_for, flash
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField, SubmitField
# from wtforms.validators import DataRequired


bp_login = Blueprint('bp_login', __name__, url_prefix='/', template_folder='templates')

# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(message='taramram')])
#     password = PasswordField('Password', validators=[DataRequired(message='tararam2')])
#     remember_me = BooleanField('Remember Me')
#     submit = SubmitField('Sign In')



@bp_login.route("/", methods=['GET', 'POST'])
def login():
    print("leroele")   
    form='leonrdo'
    return render_template('formLogin.html', form=form)
        


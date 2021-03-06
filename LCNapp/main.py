from flask import Flask, render_template, g, redirect, url_for, Blueprint, request, session

from . import db
# from LCNapp.auth import login_required, teacher_required

bp = Blueprint("main", __name__)

# route for index template


@bp.route('/')
def index():

    return render_template('layouts/index.html')


@bp.route('/menus', method=('GET'))
def main_menu():

    return render_template('layouts/menus.html')

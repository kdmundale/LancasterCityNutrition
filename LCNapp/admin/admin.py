from flask import Flask, render_template, g, redirect, url_for, Blueprint, request, session, abort
from datetime import datetime

from flask import flash
from LCNapp import db
from LCNapp.auth import login_required, admin_required

bp = Blueprint("admin", __name__)


@bp.route("/admin", methods=['GET', 'POST'])
@login_required
@admin_required
def admin_home():

    return render_template("layouts/adminHome.html")

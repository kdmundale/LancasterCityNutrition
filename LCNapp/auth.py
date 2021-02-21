import functools
import bcrypt
import datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from .forms import LoginForm

from . import db
bp = Blueprint("auth", __name__)


def hash_pass(password):
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed


def return_shake_menu(x, cur):
    cur.execute("""SELECT name FROM shakes
                WHERE shake_group = %s
                AND available = True
                ORDER BY name ASC""",
                (x,))
    shakes = cur.fetchall()
    return shakes


@bp.route('/', methods=('GET', 'POST'))
def login():

    form = LoginForm(request.form)

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        cur = db.get_db().cursor()
        error = None
        cur.execute(
            'SELECT * FROM users WHERE email = %s', (email,)
        )
        user = cur.fetchone()
        cur.close()
        if user is None or not bcrypt.checkpw(password.encode('utf8'), user['password'].tobytes()):
            error = 'Incorrect email or password!'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            total = int(user['total_login']) + 1
            user_id = user['id']
            now = datetime.datetime.now()
            day = now.strftime("%Y-%m-%d")

            con = db.get_db()
            cur = con.cursor()
            cur.execute("""UPDATE users
                            SET last_login = %s, total_login = %s
                            WHERE id = %s""",
                        (day, total, user_id))
            g.db.commit()
            cur.close()
            con.close()

            if session['user_id'] == user['id'] and user['role'] == 'member':
                return redirect(url_for('member.member_home'))
            elif session['user_id'] == user['id'] and user['role'] == 'store':
                return redirect(url_for('store.store_home'))
            elif session['user_id'] == user['id'] and user['role'] == 'admin':
                return redirect(url_for('admin.admin_home'))

        flash(error)

    cur = db.get_db().cursor()

    shake1 = return_shake_menu(1, cur)
    shake2 = return_shake_menu(2, cur)
    shake3 = return_shake_menu(3, cur)
    shake4 = return_shake_menu(4, cur)
    shake5 = return_shake_menu(5, cur)
    shake6 = return_shake_menu(6, cur)
    shake7 = return_shake_menu(7, cur)
    shake8 = return_shake_menu(8, cur)
    shake9 = return_shake_menu(9, cur)
    shake10 = return_shake_menu(10, cur)
    cur.close()

    return render_template('layouts/index.html', s1=shake1, s2=shake2, s3=shake3, s4=shake4, s5=shake5, s6=shake6,
                           s7=shake7, s8=shake8, s9=shake9, s10=shake10, form=form)


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    cur = db.get_db().cursor()

    if user_id is None:
        g.user = None
    else:
        cur.execute(
            'SELECT * FROM users WHERE id = %s', (user_id,)
        )
        g.user = cur.fetchone()
        cur.close()
    cur.close()


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


def admin_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user['role'] != 'admin':
            return redirect(url_for('user.member_home'))
        return view(**kwargs)
    return wrapped_view


def member_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user['role'] != 'member':
            return redirect(url_for('user.guest_view'))
        return view(**kwargs)
    return wrapped_view


def store_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user['role'] != 'store':
            return redirect(url_for('user.guest_view'))
        return view(**kwargs)
    return wrapped_view

import functools
import bcrypt
import re

from datetime import date
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from . import db
bp = Blueprint("register", __name__)


def valid_email(email):
    if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z", email, re.IGNORECASE):
        return 1
    else:
        return 0


def pass_check(x):
    if len(x) < 8:
        return 4
    elif re.search('[0-9]', x) is None:
        return 3
    elif re.search('[A-Z]', x) is None:
        return 2
    else:
        return 1


def hash_pass(password):
    password = password.encode('utf8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email = request.form['email']
        fName = request.form['fName']
        lName = request.form['lName']
        dob = request.form['dob']
        phone = request.form['phone']
        password = request.form['password']
        pass_confirm = request.form['pass_confirm']
        today = date.today()
        total = 1
        role = "member"

        if not email:
            error = "Please fill out your email"
        elif not fName:
            error = "Please fill out your first name"
        elif not lName:
            error = "Please fill out your last name"
        else:
            con = db.get_db()
            cur = con.cursor()
            cur.execute("""SELECT * FROM users WHERE email = %s""",
                        (email,))
            user = cur.fetchone()

            if user is not None:
                error = "An account with that email already exists"

            elif user is None:

                if password != pass_confirm:
                    error = "Passwords did not match"
                else:
                    if pass_check(password) == 4:
                        error = "Please be sure your password is at least 8 characters"
                    elif pass_check(password) == 3:
                        error = "Please be sure your password contains at least 1 number"
                    elif pass_check(password) == 2:
                        error = "Please be sure your password contains at least 1 capital letter"
                    elif pass_check(password) == 1:
                        password = hash_pass(password)

                        if valid_email(email) == 0:
                            error = "Make sure you entered a valid email"
                        else:

                            if not dob and not phone:
                                con = db.get_db()
                                cur = con.cursor()
                                cur.execute("""INSERT INTO users (email, password, first_name, last_name,
                                            total_login, role)
                                            VALUES (%s,%s,%s,%s,%s,%s)""",
                                            (email, password, fName, lName, total, role))
                                g.db.commit()
                                cur.close()
                                con.close()

                                return redirect(url_for('auth.login', email=email))

                            elif not phone:
                                con = db.get_db()
                                cur = con.cursor()
                                cur.execute("""INSERT INTO users (email, password, first_name, last_name,
                                            dob, total_login, role)
                                            VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                                            (email, password, fName, lName, dob, total, role))
                                g.db.commit()
                                cur.close()
                                con.close()

                                return redirect(url_for('auth.login', email=email))

                            elif not dob:
                                con = db.get_db()
                                cur = con.cursor()
                                cur.execute("""INSERT INTO users (email, password, first_name, last_name,
                                            total_login, role, phone)
                                            VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                                            (email, password, fName, lName, total, role, phone))
                                g.db.commit()
                                cur.close()
                                con.close()

                                return redirect(url_for('auth.login', email=email))

                            else:

                                con = db.get_db()
                                cur = con.cursor()
                                cur.execute("""INSERT INTO users (email, password, first_name, last_name,
                                            dob, total_login, role, phone)
                                            VALUES (%s,%s,%s,%s,%s,%s,%s, %s)""",
                                            (email, password, fName, lName, dob, total, role, phone))
                                g.db.commit()
                                cur.close()
                                con.close()

                                return redirect(url_for('auth.login', email=email))

            cur.close()
            con.close()

        flash(error)

        return render_template('layouts/register.html', email=email, fName=fName, lName=lName, phone=phone, dob=dob)

    return render_template('layouts/register.html')

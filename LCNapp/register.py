import functools
import bcrypt
import re

from datetime import date
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from .forms import ContactForm

from . import db
bp = Blueprint("register", __name__)

# bcrypt.checkpw(password.encode('utf8'), user['password'].tobytes()


def hash_pass(password):
    password = password.encode('utf8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed


@bp.route('/register', methods=('GET', 'POST'))
def register():

    form = ContactForm(request.form)

    if form.validate_on_submit():
        email = form.email.data
        fName = form.fName.data
        lName = form.lName.data
        dob = form.dob.data
        phone = form.phone.data
        password = hash_pass(form.password.data)
        today = date.today()
        total = 0
        role = "member"

        con = db.get_db()
        cur = con.cursor()
        cur.execute("""SELECT * FROM users WHERE email = %s""",
                    (email,))
        user = cur.fetchone()

        if user is not None:
            error = "An account with that email already exists"

        elif user is None:

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

                return redirect(url_for('auth.login'))

            elif dob and not phone:
                con = db.get_db()
                cur = con.cursor()
                cur.execute("""INSERT INTO users (email, password, first_name, last_name,
                            dob, total_login, role)
                            VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                            (email, password, fName, lName, dob, total, role))
                g.db.commit()
                cur.close()
                con.close()

                return redirect(url_for('auth.login'))

            elif phone and not dob:
                con = db.get_db()
                cur = con.cursor()
                cur.execute("""INSERT INTO users (email, password, first_name, last_name,
                            total_login, role, phone)
                            VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                            (email, password, fName, lName, total, role, phone))
                g.db.commit()
                cur.close()
                con.close()

                return redirect(url_for('auth.login'))

            else:
                print('doing it!')
                con = db.get_db()
                cur = con.cursor()
                cur.execute("""INSERT INTO users (email, password, first_name, last_name,
                             dob, total_login, role, phone)
                             VALUES (%s,%s,%s,%s,%s,%s,%s, %s)""",
                            (email, password, fName, lName, dob, total, role, phone))
                g.db.commit()
                cur.close()
                con.close()

                return redirect(url_for('auth.login'))

        cur.close()
        con.close()
        flash(error)
        return render_template('layouts/register.html', form=form)

    else:
        error = "form not submitted"
        flash(error)
        return render_template('layouts/register.html', form=form)

from flask import Flask, render_template, g, redirect, url_for, Blueprint, request, session, abort
import datetime

from flask import flash
from LCNapp import db
from LCNapp.auth import login_required, admin_required
from LCNapp.forms import AddItem

bp = Blueprint("admin", __name__)


def getDate(x):
    date_obj = datetime.datetime.strptime(x, '%Y-%m-%d')
    date = date_obj.strftime("%a %m/%d/%Y")
    return date


@bp.route("/admin", methods=['GET', 'POST'])
@login_required
@admin_required
def admin_home():

    now = datetime.datetime.now()
    day = now.strftime("%Y-%m-%d")
    con = db.get_db()
    cur = con.cursor()
    cur.execute("""SELECT SUM(daily_total) FROM daily""")
    total_shakes = cur.fetchone()
    cur.execute("""SELECT SUM(daily_total)
                    FROM daily
                    WHERE day = %s""",
                (day,))
    shakes_today = cur.fetchone()
    cur.close()
    con.close()

    return render_template("layouts/admin/adminHome.html", total_shakes=total_shakes,
                           shakes_today=shakes_today)


@bp.route("/admin/store_reports", methods=['GET', 'POST'])
@login_required
@admin_required
def admin_store_reports():

    now = datetime.datetime.now()
    day = now.strftime("%Y-%m-%d")

    con = db.get_db()
    cur = con.cursor()
    cur.execute("""SELECT d.shake_id, s.name as name, SUM(d.daily_total) AS total_sales
                FROM daily d
                JOIN shakes s on s.id = d.shake_id
                WHERE day BETWEEN %s and %s
                GROUP BY name, shake_id
                ORDER BY total_sales DESC""",
                (day, day))
    shakes = cur.fetchall()
    cur.execute("""SELECT SUM(daily_total)
                FROM daily
                WHERE day BETWEEN %s AND %s""",
                (day, day))
    total = cur.fetchone()
    cur.close()

    day = getDate(day)

    if request.method == 'POST':

        sDate = request.form['sDate']
        eDate = request.form['eDate']

        con = db.get_db()
        cur = con.cursor()
        cur.execute("""SELECT d.shake_id, s.name as name, SUM(d.daily_total) AS total_sales
                    FROM daily d
                    JOIN shakes s on s.id = d.shake_id
                    WHERE day BETWEEN %s and %s
                    GROUP BY name, shake_id
                    ORDER BY total_sales DESC""",
                    (sDate, eDate))
        shakes = cur.fetchall()
        cur.execute("""SELECT SUM(daily_total)
                    FROM daily
                    WHERE day BETWEEN %s AND %s""",
                    (sDate, eDate))
        total = cur.fetchone()
        cur.close()
        con.close()

        sDate = getDate(sDate)
        eDate = getDate(eDate)

        return render_template("layouts/admin/store_reports.html", shakes=shakes,
                               sDate=sDate, eDate=eDate, total=total)
    con.close()

    return render_template("layouts/admin/store_reports.html", shakes=shakes,
                           sDate=day, eDate=day, total=total)


@bp.route("/admin/member_info", methods=['GET', 'POST'])
@login_required
@admin_required
def member_info():

    con = db.get_db()
    cur = con.cursor()
    cur.execute("""SELECT COUNT(*) FROM users""")
    total_users = cur.fetchone()

    cur.execute("""SELECT first_name, last_name, email, phone, dob, register_date, last_login, total_login
                    FROM users
                    WHERE role = 'member'
                    ORDER BY total_login DESC
                    LIMIT 10""")
    user_login_freq = cur.fetchall()

    cur.execute("""SELECT h.user_id, u.email, SUM(h.this_shake) AS total
                    FROM has_had h
                    JOIN (SELECT u.id, u.email
                    FROM users u) u ON u.id = h.user_id
                    GROUP BY h.user_id, u.email
                    ORDER BY total DESC
                    LIMIT 10""")
    user_shake_freq = cur.fetchall()

    cur.execute("""SELECT first_name, last_name, email, phone, dob, register_date, last_login, total_login FROM users
                    ORDER BY last_name ASC""")
    all_users = cur.fetchall()

    cur.execute("""SELECT first_name, last_name, email, phone, dob, register_date, last_login, total_login FROM users
                    WHERE phone IS NOT NULL
                    ORDER BY last_name ASC""")
    user_phone = cur.fetchall()

    cur.close()
    con.close()

    return render_template("layouts/admin/member_info.html", total_users=total_users,
                           user_login_freq=user_login_freq, user_shake_freq=user_shake_freq,
                           all_users=all_users, user_phone=user_phone)


@bp.route("/admin/shake_menu", methods=['GET', 'POST'])
@login_required
@admin_required
def admin_shake_menu():

    form = AddItem(request.form)

    con = db.get_db()
    cur = con.cursor()
    cur.execute("""SELECT * FROM shakes WHERE available = True""")
    all_shakes = cur.fetchall()

    cur.execute("""SELECT * FROM shakes WHERE available = False""")
    not_shakes = cur.fetchall()

    return render_template("layouts/admin/shake_menu.html", all_shakes=all_shakes, not_shakes=not_shakes, form=form)

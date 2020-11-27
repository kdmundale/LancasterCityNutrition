import datetime

from flask import Flask, render_template, g, redirect, url_for, Blueprint, request, session, abort

from LCNapp import db
from LCNapp.auth import login_required, member_required
from LCNapp.admin.admin import getDate

bp = Blueprint("member", __name__)


@bp.route("/member", methods=['GET'])
@login_required
@member_required
def member_home():

    user_id = session.get('user_id')
    con = db.get_db()
    cur = con.cursor()
    cur.execute("""SELECT s.name as shake_name, h.rating as shake_rating, h.comment as shake_comment, h.this_shake as shake_freq
                    FROM shakes s
                    JOIN has_had h on s.id = h.shake_id
                    WHERE h.user_id = %s
                    ORDER BY shake_rating DESC
                    LIMIT 5""",
                (user_id,))
    member_top_5 = cur.fetchall()
    cur.execute("""SELECT COUNT(*)
                    FROM has_had
                    WHERE user_id = %s;""",
                (user_id,))
    diff_shakes = cur.fetchone()
    cur.execute("""SELECT SUM(this_shake)
                    FROM has_had
                    WHERE user_id = %s;""",
                (user_id,))
    total_shakes = cur.fetchone()
    cur.execute("""SELECT id, name FROM shakes WHERE available = True""")
    all_shakes = cur.fetchall()
    cur.execute("""SELECT s.id, s.name FROM shakes s
                JOIN has_had h on s.id = h.shake_id
                WHERE h.user_id = %s""",
                (user_id,))
    had_shakes = cur.fetchall()

    cur.execute("""SELECT id, name FROM shakes s
                    WHERE id <> ALL (SELECT s.id FROM shakes s
                                JOIN has_had h on s.id = h.shake_id
                                WHERE h.user_id = %s)""",
                (user_id,))
    havent_had = cur.fetchall()
    cur.close()
    con.close()

    return render_template("layouts/member/userHome.html", member_top_5=member_top_5,
                           diff_shakes=diff_shakes, total_shakes=total_shakes,
                           all_shakes=all_shakes, had_shakes=had_shakes,
                           havent_had=havent_had)


@bp.route("/member/add_shakes", methods=['GET'])
@login_required
@member_required
def member_add_shake():

    like = '(a|b|c|d)%'
    like2 = '(e|f|g|h)%'
    like3 = '(i|j|k|l)%'
    like4 = '(m|n|o|p)%'
    like5 = '(q|r|s|t|u)%'
    like6 = '(v|w|x|y|z)%'

    def getShakes(x):
        cur.execute("""SELECT * FROM shakes
                    WHERE lower(name) SIMILAR TO %s
                    AND available = True
                    ORDER BY name ASC""",
                    (x,))
        shakes = cur.fetchall()
        return shakes

    con = db.get_db()
    cur = con.cursor()
    shakes = getShakes(like)
    shakes1 = getShakes(like2)
    shakes2 = getShakes(like3)
    shakes3 = getShakes(like4)
    shakes4 = getShakes(like5)
    shakes5 = getShakes(like6)
    cur.close()
    con.close()
    return render_template("layouts/member/member_shake.html", shakes=shakes,
                           shakes1=shakes1, shakes2=shakes2, shakes3=shakes3,
                           shakes4=shakes4, shakes5=shakes5)


@bp.route("/member/account", methods=['GET'])
@login_required
@member_required
def member_info():

    user_id = session.get('user_id')
    con = db.get_db()
    cur = con.cursor()
    cur.execute("""SELECT first_name, last_name, email, phone, dob, register_date, last_login
                    FROM users
                    WHERE id = %s""",
                (user_id,))
    user_info = cur.fetchone()
    cur.close()
    con.close()

    sDate = user_info['register_date'].strftime("%a %m/%d/%Y")
    lDate = user_info['last_login'].strftime("%a %m/%d/%Y")
    bDate = user_info['dob'].strftime("%m/%d")

    return render_template("layouts/member/member_info.html", user_info=user_info, lDate=lDate, sDate=sDate)


@bp.route("/member/account/change_password", methods=['GET'])
@login_required
@member_required
def change_password():

    return render_template("")

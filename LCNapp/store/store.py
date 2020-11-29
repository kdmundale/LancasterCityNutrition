from flask import Flask, render_template, g, redirect, url_for, Blueprint, request, session, abort
from datetime import datetime

from flask import flash
from LCNapp import db
from LCNapp.auth import login_required, store_required

bp = Blueprint("store", __name__)


@bp.route("/store", methods=['GET', 'POST'])
@login_required
@store_required
def store_home():

    now = datetime.now()
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

    return render_template("layouts/store/store.html", total_shakes=total_shakes, shakes_today=shakes_today)


@bp.route("/store_shakes", methods=['GET', 'POST'])
@login_required
@store_required
def store_shakes():

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

    if request.method == 'POST':

        now = datetime.now()
        day = now.strftime("%Y-%m-%d")
        shake_id = request.form.getlist('shake_id[]')
        nums = request.form.getlist('num_shakes[]')
        pairs = []
        for i, n in enumerate(nums):
            if n != "":
                pairs.append([int(shake_id[i]), int(n)])

        for pair in pairs:

            shake_id = pair[0]
            total = pair[1]

            cur = con.cursor()
            cur.execute("""SELECT * FROM daily
                            WHERE shake_id = %s
                            AND day = %s""",
                        (shake_id, day))
            any = cur.fetchone()
            cur.close()

            if any is not None:
                date_id = any[0]
                total = int(any[3]) + total
                cur = con.cursor()
                cur.execute("""UPDATE daily SET daily_total = %s
                                WHERE id = %s""",
                            (total, date_id))
                g.db.commit()
                cur.close()

            else:

                cur = con.cursor()
                cur.execute("""INSERT INTO daily (day, shake_id, daily_total)
                                VALUES (%s,%s,%s)""",
                            (day, shake_id, total))
                g.db.commit()
                cur.close()

    cur.close()
    con.close()
    return render_template("layouts/store/store_shake.html", shakes=shakes,
                           shakes1=shakes1, shakes2=shakes2, shakes3=shakes3,
                           shakes4=shakes4, shakes5=shakes5)

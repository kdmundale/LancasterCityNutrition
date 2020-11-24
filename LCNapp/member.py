from flask import Flask, render_template, g, redirect, url_for, Blueprint, request, session, abort

from . import db
from LCNapp.auth import login_required, member_required

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

    return render_template("layouts/userHome.html", member_top_5=member_top_5,
                           diff_shakes=diff_shakes, total_shakes=total_shakes,
                           all_shakes=all_shakes, had_shakes=had_shakes,
                           havent_had=havent_had)

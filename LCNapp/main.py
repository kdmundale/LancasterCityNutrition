from flask import Flask, render_template, g, redirect, url_for, Blueprint, request, session

from . import db
# from LCNapp.auth import login_required, teacher_required

bp = Blueprint("main", __name__)

# route for index template


@bp.route('/')
def index():
    return render_template('layouts/index.html')


# @bp.route('/member', methods=['GET'])
# @login_required
# @member_required
# def memebr_home():
#     user_id = session['user_id']


# route for showing the home for teachers


# @bp.route("/home", methods=['GET'])
# @login_required
# @teacher_required
# def home():
#     # user_id = session['user_id']
#     cur = db.get_db().cursor()
#     cur.execute(
#         """SELECT courses.course_id, courses.name, courses.major, users.name AS teacher_name FROM courses INNER JOIN users ON courses.teacherid = users.id""")
#     courses = cur.fetchall()
#     cur.close()
#
#     return render_template("layouts/home.html", courses=courses)
#
#
# @bp.route("/home/mycourses", methods=['GET'])
# @login_required
# @teacher_required
# def my_courses():
#
#     user_id = session.get('user_id')
#
#     cur = db.get_db().cursor()
#     cur.execute(
#         """SELECT courses.course_id, courses.name, courses.major,
#         users.name AS teacher_name FROM courses
#         INNER JOIN users ON courses.teacherid = users.id
#         WHERE users.id = %s """,
#         (user_id,))
#
#     courses = cur.fetchall()
#     cur.close()
#
#     return render_template("layouts/home.html", courses=courses)
#
#
# @bp.route("/course/<int:course_id>/session/<int:session_id>/assignments/<int:assignment_id>/grades")
# @login_required
# @teacher_required
# def teacher_assignment_grades(course_id, session_id, assignment_id):
#     """View for the teacher to view assignments in a course."""
#
#     con = db.get_db()
#     cur = con.cursor()
#
#     cur.execute("""
#     SELECT (ROUND(grades.points_received/grades.total_points, 2 )*100) AS assignment_grade,
#     grades.total_points, grades.points_received, grades.grade_id, users.name
#     FROM grades INNER JOIN users
#     ON (grades.student_id = users.id)
#     WHERE assignment_id = %s;
#     """,
#                 (assignment_id,))
#
#     grades = cur.fetchall()
#
#     return render_template('layouts/gradebook/teacher_view.html', grades=grades,
#                            course_id=course_id, session_id=session_id, assignment_id=assignment_id)
#
#
# @bp.route("/course/<int:course_id>/session/<int:session_id>/assignments/<int:assignment_id>/input-grade/<int:grade_id>", methods=('GET', 'POST'))
# @login_required
# @teacher_required
# def input_grade(course_id, session_id, assignment_id, grade_id):
#     """View for teacher to update assignment grade."""
#
#     con = db.get_db()
#     cur = con.cursor()
#
#     cur.execute("""
#     SELECT grades.total_points, grades.assignment_id AS assign,
#     users.name AS student
#     FROM grades JOIN users ON users.id = grades.student_id
#     WHERE grade_id = %s
#     """,
#                 (grade_id,))
#
#     max_points = cur.fetchone()
#
#     if request.method == 'POST':
#
#         grade_input = request.form['grade_input']
#         feedback = request.form['feedback']
#
#         cur.execute("""
#         UPDATE grades SET points_received = %s, feedback = %s
#         WHERE grade_id = %s
#         """, (grade_input, feedback, grade_id))
#         g.db.commit()
#
#         cur.close()
#         con.close()
#
#         return redirect(url_for('main.teacher_assignment_grades', course_id=course_id,
#                                 session_id=session_id, assignment_id=assignment_id))
#
#     cur.close()
#     con.close()
#
#     return render_template('layouts/gradebook/input_grade.html', max_points=max_points)

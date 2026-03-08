import os
from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)
app.secret_key = "franklins-demo-secret-key"

# simples data for demo purposes
COURSES = [
    {
        "id": 1,
        "title": "Life Skill And Professional Communication",
        "category": "UCHUT128",
        "price": "2999.00",
    },
    {
        "id": 2,
        "title": "Health And Wellness",
        "category": "UCPWT127",
        "price": "2999.00",
    },
    {
        "id": 3,
        "title": "Algorithmic Thinking with python",
        "category": "UCEST105",
        "price": "2999.00",
    },
    {
        "id": 4,
        "title": "Introduction to Electrical Engineering",
        "category": "GXEST104",
        "price": "2999.00",
    },
]

BTECH_DEPARTMENTS = [
    {"name": "Computer Science & Engineering", "slug": "cse"},
    {"name": "Mechanical Engineering", "slug": "me"},
    {"name": "Electronics & Communication Engineering", "slug": "ece"},
    {"name": "Electrical & Electronics Engineering", "slug": "eee"},
    {"name": "Civil Engineering", "slug": "ce"},
    {"name": "Aeronautical Engineering", "slug": "ae"},
    {"name": "Agricultural Engineering", "slug": "agri"},
    {"name": "Applied Electronics & Instrumentation", "slug": "aei"},
]

SEMESTERS = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"]

def get_department_by_slug(department_slug):
    """Return department dict by slug, or None if not found."""
    for department in BTECH_DEPARTMENTS:
        if department["slug"] == department_slug:
            return department
    return None


@app.route("/")
def home():
    # show first few as featured
    featured_courses = COURSES[:3]
    return render_template("home.html", featured_courses=featured_courses)


@app.route("/courses")
def courses():
    return render_template("courses.html", courses=COURSES)


@app.route("/departments")
def departments():
    return render_template("departments.html", departments=BTECH_DEPARTMENTS)


@app.route("/departments/<string:department_slug>/semesters")
def department_semesters(department_slug):
    department = get_department_by_slug(department_slug)
    if department is None:
        return render_template("404.html"), 404

    return render_template(
        "semesters.html",
        department=department,
        semesters=SEMESTERS,
    )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    message = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        # demo-only validation
        if username and password:
            flash(f"Welcome back, {username}!", "success")
            return redirect(url_for("home"))
        message = "Please enter both username and password."

    return render_template("login.html", message=message)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
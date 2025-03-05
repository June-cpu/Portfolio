from flask import Flask, render_template, redirect, url_for
from config import Config
from models import db, Project
from forms import AddProjectForm

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Create tables if they don't exist
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/projects")
def show_projects():
    projects = Project.query.all()
    return render_template("projects.html", projects=projects)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/admin", methods=["GET", "POST"])
def admin():
    form = AddProjectForm()
    if form.validate_on_submit():
        new_project = Project(
            title=form.title.data,
            description=form.description.data,
            github_url=form.github_url.data
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for("show_projects"))
    # Show existing projects in admin page
    projects = Project.query.all()
    return render_template("admin.html", form=form, projects=projects)


@app.route("/delete_project/<int:project_id>", methods=["POST"])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("admin"))


if __name__ == "__main__":
    app.run(debug=True)

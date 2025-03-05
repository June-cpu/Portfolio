from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL, Optional

class AddProjectForm(FlaskForm):
    title = StringField("Project Title", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    github_url = StringField("GitHub URL", validators=[Optional(), URL()])
    submit = SubmitField("Add Project")

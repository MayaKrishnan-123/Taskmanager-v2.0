# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError,SelectField
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Employee,Task


class TaskForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    status = SelectField('Status',choices = [('C', 'Created'),
      ('P', 'In progress'),('D','Deleted')])
    importance = SelectField('How Important it is?', choices=[('H', 'HIGH'),
                                            ('M', 'Medium'), ('L', 'Low')])
    towhom = StringField('To Whom it is assigned?',validators=[DataRequired()])

    submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Add Employee!!')

    def validate_email(self, field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')

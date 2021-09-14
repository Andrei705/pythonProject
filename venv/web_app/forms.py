from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class CompletionBD(FlaskForm):
    folder = StringField('Имя папки', validators=[DataRequired()])
    type_one = StringField('Тип1', validators=[DataRequired()])
    type_two = StringField('Тип2', validators=[DataRequired()])
    submit = SubmitField('Отправить')

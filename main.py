from datetime import date, datetime

from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from db_init import global_init, create_session
from db_class import User, Jobs
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class UserForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    position = StringField('Должность', validators=[DataRequired()])
    speciality = StringField('Специальность', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password', message='Пароли не совпадают')])
    submit = SubmitField('Добавить пользователя')

db_name = "database.db"
session_factory = global_init(db_name)
session = create_session(session_factory)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
def index():
    jobs = session.query(Jobs).all()
    return render_template('job.html', jobs=jobs)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        session.add(User(surname=form.surname.data, name=form.name.data, age=form.age.data, position=form.position.data, speciality=form.speciality.data, address=form.address.data, email=form.email.data, hashed_password=form.password.data, modified_date=datetime.now()))
        session.commit()
    return render_template('reg.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='127.0.0.1')
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField,IntegerField
from wtforms.validators import Length, Email, EqualTo, Required,URL,NumberRange
from simpledu.models import db, User,Course
from wtforms import ValidationError

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(3, 24)])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('Password again', validators=[Required(), EqualTo('password')])
    submit = SubmitField('Submit')

    def validate_username(self, field):
        if not field.data.isalnum():
            raise ValidationError('only alphabeta and number')
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('username used')
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('email used')
    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('Remember me')
    def validate_email(self, field):
        if field.data and not User.query.filter_by(username=field.data).first():
            raise ValidationError('username not register')

    def validate_password(self, field):
        user = User.query.filter_by(username=self.username.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('Password error')
    submit = SubmitField('Submit')


class CourseForm(FlaskForm):
    name=StringField('CourseName',validators=[Required(),Length(5,32)])
    description=TextAreaField('CourseDescription',validators=[Required(),Length(20,256)])
    image_url=StringField('FrontImage',validators=[Required(),URL()])
    author_id=IntegerField('AuthorId',validators=[Required(),NumberRange(min=1,message='Error ID')])
    submit=SubmitField('Submit')

    def validate_author_id(self,field):
        if not User.query.get(self.author_id.data):
            raise ValidationError('User not exist')

    def create_course(self):
        course=Course()
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

    def update_course(self,course):
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

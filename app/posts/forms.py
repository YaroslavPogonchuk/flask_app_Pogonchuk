from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, SelectField, DateField
from wtforms.validators import DataRequired, Length

CATEGORIES = [("tech","Tech"),("science","Science"),("lifestyle","Lifestyly")]

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(),Length(min=2,)])
    content = TextAreaField("Content", validators=[DataRequired()],render_kw={"rows":4, "cols":4})
    is_active = BooleanField('Active Post')
    publish_date = DateField('Publish Date',validators=[DataRequired()])
    category = SelectField("Category",validators=[DataRequired()],choices=CATEGORIES)
    submit = SubmitField("Add Post")
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextField, FileField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class PropertyForm(FlaskForm):
    title = TextField("Property Title", validators = [DataRequired()])
    description = TextAreaField("Property Description", validators = [DataRequired()])
    rooms = TextField("No. of Rooms", validators = [DataRequired()])
    bathrooms = TextField("No. of Bathrooms", validators = [DataRequired()])
    price = TextField("Price", validators = [DataRequired()])
    property_type = SelectField("Property Type", choices = [('House', 'House'), ('Apartment', 'Apartment')], validators = [DataRequired()])
    location = TextField("Location", validators = [DataRequired()])
    photo = FileField("Photo", validators=[FileRequired(), FileAllowed(['jpg','png'],'Images only!')])
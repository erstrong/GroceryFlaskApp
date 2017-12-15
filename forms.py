from flask_wtf import Form
from wtforms import IntegerField, BooleanField, StringField
from wtforms.validators import DataRequired

class Forecast(Form):
    date1 = StringField('date1', validators=[DataRequired()])
    #date2 = StringField('date2')
    store_nbr = IntegerField('store_nbr', validators=[DataRequired()])
    item_nbr = IntegerField('item_nbr')
    class_id = IntegerField('class_id')
    onpromotion = BooleanField('onpromotion', default=False)
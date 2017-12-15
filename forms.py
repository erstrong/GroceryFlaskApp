from flask_wtf import Form
from wtforms import IntegerField, BooleanField, DateField

class Forecast(Form):
    date1 = DateField('date1')
    date2 = DateField('date2')
    store_nbr = IntegerField('store_nbr')
    item_nbr = IntegerField('item_nbr')
    class_id = IntegerField('class_id')
    onpromotion = BooleanField('onpromotion', default=False)
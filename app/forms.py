from flask_wtf import FlaskForm
import wtforms as ws

class TransactionForm(FlaskForm):
    unit_list = ['доллар','евро', 'сом', 'рубль']
    status_list = ['выполнена', 'не выполнена']
    period = ws.StringField('Период', validators=[ws.validators.DataRequired(), ])
    value = ws.IntegerField('Сумма', validators=[ws.validators.DataRequired(), ])
    status = ws.SelectField('Статус',choices=[e for e in status_list], validators=[ws.validators.DataRequired(), ])
    unit = ws.SelectField('Валюта',choices=[e for e in unit_list], validators=[ws.validators.DataRequired(), ])
    subject = ws.StringField('Комментария', validators=[ws.validators.DataRequired(), ])




class UserForm(FlaskForm):
    username = ws.StringField('Имя пользователя', validators=[ws.validators.DataRequired(),
                                                              ws.validators.Length(min=4,max=20)] )
    password = ws.PasswordField('Пароль', validators=[ws.validators.DataRequired(),
                                                      ws.validators.Length(min=8,max=24)] )

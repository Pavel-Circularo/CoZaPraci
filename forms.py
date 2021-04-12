from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddJob(FlaskForm):

    name = StringField('Jméno tvé pozice:')
    prejudice = StringField('Co si lidé myslí, že děláš?')
    reality = StringField('Co opravdu v práci děláš?')
    day_in_life = StringField('Jak vypadá tvůj standartní pracovní den?')
    salary = StringField('Jaký je tvůj plat?')
    education = StringField('Je třeba k této práci nějaké vzdělání? Pokud ano, jaké?')
    submit = SubmitField('Přidat záznam')

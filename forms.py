from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField

class AddJob(FlaskForm):

    name = TextAreaField('Jméno tvé pozice:')
    prejudice = TextAreaField('Co si lidé myslí, že děláš?')
    reality = TextAreaField('Co opravdu v práci děláš?')
    day_in_life = TextAreaField('Jak vypadá tvůj standartní pracovní den?')
    salary = TextAreaField('Jaký je tvůj plat?')
    education = TextAreaField('Je třeba k této práci nějaké vzdělání? Pokud ano, jaké?')
    submit = SubmitField('Přidat záznam')

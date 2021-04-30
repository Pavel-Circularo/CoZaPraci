import os
from forms import AddJob
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    prejudice = db.Column(db.Text)
    reality = db.Column(db.Text)
    day_in_life = db.Column(db.Text)
    salary = db.Column(db.Text)
    education = db.Column(db.Text)

    def __init__(self, name, prejudice, reality, day_in_life, salary, education):
        self.name = name
        self.prejudice = prejudice
        self.reality = reality
        self.day_in_life = day_in_life
        self.salary = salary
        self.education = education

    def __repr__(self):
        return f"Práce: {self.name}, {self.prejudice}, {self.reality}, {self.day_in_life}, {self.salary}, {self.education}"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/domu')
def home():
    return render_template("home.html")


@app.route('/seznam')
def worklist():
    jobs = Job.query.all()
    return render_template("worklist.html", jobs=jobs)


@app.route('/dekujeme')
def thank_you():
    return render_template("thankyou.html")


@app.route("/pridat_praci", methods=['GET', 'POST'])
def add_job():
    form = AddJob()

    if form.validate_on_submit():
        name = form.name.data
        prejudice = form.prejudice.data
        reality = form.reality.data
        day_in_life = form.day_in_life.data
        salary = form.salary.data
        education = form.education.data

        new_job = Job(name, prejudice, reality, day_in_life, salary, education)
        db.session.add(new_job)
        db.session.commit()

        return redirect(url_for('thank_you'))
    return render_template("pridat_praci2.html", form=form)

@app.route('/popis_pozice/<int:job_id>')
def job_desc(job_id):
    jobs = Job.query.all()
    my_job = Job.query.filter(Job.id == job_id).first_or_404()
    return render_template("job_desc.html", my_job = my_job, jobs = jobs)


if __name__ == '__main__':
    app.run(debug=True)

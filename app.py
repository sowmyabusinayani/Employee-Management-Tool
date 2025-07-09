from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    job_title = db.Column(db.String(100), nullable=False)
    hire_date = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Employee {self.name}>'

@app.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    department = request.form['department']
    job_title = request.form['job_title']
    hire_date = request.form['hire_date']
    new_employee = Employee(name=name, department=department, job_title=job_title, hire_date=hire_date)
    db.session.add(new_employee)
    db.session.commit()
    flash('Employee added successfully')
    return redirect(url_for('index'))

def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)

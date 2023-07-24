from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sandy'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sandy.sqlite'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(180), nullable=False)
    last_name = db.Column(db.String(110), nullable=False)
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            return redirect(url_for('secret_page'))

        flash('Invalid credentials', 'error')

    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Wrong password Please try again.', 'error')
            return redirect(url_for('signup'))

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email ID already exists', 'error')
            return redirect(url_for('signup'))

        new_user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('thankyou'))

    return render_template('signup.html')

@app.route('/secret', methods=['GET', 'POST'])
def secret_page():
    return render_template('secretPage.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)

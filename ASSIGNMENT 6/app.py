from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'secret_key' 


users = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if checking_password(password):
            users.append((username, password))
            return render_template('report.html', report_message='Password requirements are satisfied.')
        else:
            return render_template('report.html', report_message='Password requirements are not satisfied.')
    
    return render_template('index.html')


def checking_password(password):
    if len(password) < 8:
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not password[-1].isdigit():
        return False
    return True


if __name__ == '__main__':
    app.run(debug=True)

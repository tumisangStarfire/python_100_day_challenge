from flask import Flask, render_template
from flask_mysqldb import  MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234.qwerty?'
app.config['MYSQL_DB'] = 'flask_todo'

mysql = MySQL()
mysql.init_app(app)

cursor = mysql.get_db().cursor()




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return "Hello About"


if __name__ == "__main__":
    app.run(debug=True)
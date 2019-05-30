from flask import Flask,render_template,url_for,request,redirect
from flask_mysqldb import MySQL
from mydbkey import myDb

app = Flask(__name__)

configuration = myDb()

app.config['MYSQL_HOST']=configuration.MYQL_HOST
app.config['MYSQL_USER']=configuration.MYSQL_USER
app.config['MYSQL_PASSWORD']=configuration.MYSQL_PASSWORD
app.config['MYSQL_DB']=configuration.MYSQL_DB

mysql = MySQL(app)




@app.route('/')
def homePage():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT branch_name FROM branch''')
    rv = cur.fetchall()
    return str(rv)

@app.route('/login')
def login():
    return render_template('login.html')
    



@app.route('/report',methods=['POST'])
def report():
    name = request.form['userName']
    password = request.form['passWord']
    return 'Name: '+name+' Password: '+ password


if __name__=="__main__":
    app.run(debug=True)
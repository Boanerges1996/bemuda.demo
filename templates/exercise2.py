from flask import Flask,render_template,url_for,request

app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('homePage.html')



if __name__=="__main__":
    app.run(debug=True)
from flask import Flask,render_template

app = Flask(__name__)

POSTS = [
    {
        'author':'Boanerges',
        'title':'Blog post 1',
        'content':'First post content',
        'date_release':'April 20,2019'
    },
     {
        'author':'Samson',
        'title':'Blog post 2',
        'content':'Second post content',
        'date_release':'April 21,2019'
    }
]


@app.route('/')
def Home():
    return render_template('homePage.html', posts=POSTS)


@app.route('/about')
def about():
    return render_template('aboutUs.html', title='About')

if __name__=="__main__":
    app.run(debug=True)

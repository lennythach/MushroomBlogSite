from flask import Flask, render_template, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = '0b48418be8286fe839a399eacfe3abc7'

posts = [
    {
        'author':'Lenny Thach',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'September 17, 2021'
    },

    {
        'author':'Meiling Sproger',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'September 18, 2021'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    return render_template('register.html', title='Register')

@app.route("/login")
def login():
    return render_template('login.html', title='Login')

if __name__=='__main__':
    app.run(debug=True)
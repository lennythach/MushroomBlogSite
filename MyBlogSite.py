from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET KEY'] = '0b48418be8286fe839a399eacfe3abc7'

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
    form = RegistrationForm()
    return render_template('register.html', title= 'Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title= 'Login', form=form)

if __name__=='__main__':
    app.run(debug=True)
import re
from datetime import datetime
from app import app
from flask import render_template, request, redirect, jsonify, make_response

@app.template_filter('clean_date')
def clean_date(dt):
    return dt.strftime('%d %b %Y')

@app.route("/")
def home():

    return render_template('public/index.html')

@app.route("/sign-up",methods=['GET','POST'])
def sign_up():
    
    if request.method =='POST':
        form_data = request.form
        print(form_data)
        username = form_data['username']
        email = form_data['email']
        password = form_data['password']
        # do something with this data
        print(username,email,password)
        
        return redirect(request.url)
    
    
    return render_template('public/sign_up.html')

@app.route('/guestbook')
def guestbook():
    return render_template('public/guestbook.html')

@app.route('/guestbook/create-entry',methods=['POST'])
def create_entry():
    body = request.get_json()
    print(body)
    res = make_response(jsonify({"message":"Json recived"}),200)
    return res


@app.route('/json',methods=['POST'])
def json():
    if request.is_json:
        body = request.get_json()
        response = {
            "message":"JSON recived!",
            "sender":body["name"]
        }
        res = make_response(jsonify(response))
        print(type(body))
        print(body)
        return res
    else:
        res = make_response(jsonify({"message":"No JSON recived"}),400)
        return res

users = {
    'noam': {
        'name': 'Noam Dahan',
        'bio': 'I am Noam and I am a Software Engineer!',
        'twitter_handle': '@noam'
    },
    'yossi': {
        'name': 'Yossi Benyayoun',
        'bio': 'I am Yossi and I am a Web Developer!',
        'twitter_handle': '@yossi'
    },
    'yael': {
        'name': 'Yael Manor',
        'bio': 'I am Yael and I am a Data Scientist!',
        'twitter_handle': '@yael'
    },
    'yoni': {
        'name': 'Yoni Bloch',
        'bio': 'I am Yoni and I am a DevOps Engineer!',
        'twitter_handle': '@yoni'
    }
}

@app.route('/profile/<username>')
def profile(username):
    user=None
    if username in users:
        user = users[username]
    return render_template('public/profile.html', user=user, username=username)

@app.route('/multi/<foo>/<boo>/<moo>')
def multiple_vars(foo,boo,moo):
    return f'foo is {foo}, boo is {boo}, moo is {moo}'

@app.route("/jinja")
def jinja():
    my_name="Noam"
    age = 30
    langs = ["Python", "JavaScript", "Bash", "C++"]
    friends = {
        "Noam": 30,
        "Yossi": 31,
        "Yael": 29,
        "Yoni": 28,
        "Yiftach": 30
    }
    colors = ("Red", "Green", "Blue")
    
    html_string = '<h4> This is some HTML </h4>'
    suspicious = '<script> alert("You got hacked") </script>'
    
    cool = True
    
    now = datetime.now()
    
    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url
        def pull(self):
            return f"Pulling repo {self.name}"
        def clone(self):
            return f"Cloning into {self.url}"        
    
    def repeat(x,qty):
        return x * qty

    my_remote = GitRemote(name="Flask Jinja", description="Template design tutorial for Flask", url="https://github/boydem/learning-flask.git")
       
    return render_template('public/jinja.html',suspicious=suspicious,html_string=html_string,now=now, name=my_name , age=age, langs=langs, friends=friends, colors=colors, GitRemote=GitRemote, repeat=repeat, cool=cool, my_remote=my_remote)


@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

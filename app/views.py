import re
from datetime import datetime
from app import app
from flask import render_template, request, redirect

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
        print(username,email,password)
        
        return redirect(request.url)
    
    
    return render_template('public/sign_up.html')

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

from flask import Flask
from flask import redirect, render_template, url_for

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "hello world"

@app.route("/hi")
def hi():
    return "hi world how are you ...***"


@app.route("/name/<name>")
def name(name):
    return "hi...my name is " + name ;

@app.route("/sub")
def sub():
    a = 500
    b = 200
    c = a - b
    return c

@app.route("/blog/<int:postID>")
def blog(postID):
    return "blog number is %d"% postID  # %d is to read integers


@app.route("/rev/<float:revno>")
def revision(revno):
    return "Rev number is %f"% revno

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'
    
@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

@app.route("/user/<name>")
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))

if __name__ == '__main__':
    app.run(debug=True,port=3000)
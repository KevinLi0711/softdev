#Flying Karate Masters: Matthew Yee, Kevin Li, Joseph Wu
#SoftDev
#K19 -- Cookies
#2022-11-03
#time spent: 0.2 hours

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session

app = Flask(__name__)    #create Flask object

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

'''
@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return app.redirect(app.url_for('login'))
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        session['username'] = request.form['username']
        print("username is " + session['username'])
        print(session.keys())

        if session['username'] == 'karate': #if username is karate, you get shown the response page, otherwise it returns an error page
            print(session.__dict__)
            return render_template('response.html', username = session['username'])
        else:
            error = "username not found"
        #return app.redirect(app.url_for('index'))

    #print(session.__dict__)
    return render_template('login.html', error_message = error)
    '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    #print(session.__dict__)
    print(session.keys)
    return app.redirect(app.url_for('login'))


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()

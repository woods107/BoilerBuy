from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    #Use placeholder dummy list of posts for the moment
    #User object will contain username, real name, and contact info fields (eventually)
    #Posts will contain title, description, posting date, object of user, and a photo
    postings = [
            {
                'user': {'name': 'jane'},
                'title': 'Test Title 1', 
                'desc': 'Test Description 1'
            },        
            {
                'user': {'name': 'joseph'},
                'title': 'Test Title 2',
                'desc': 'Test Description 2'
            }
    ]
    return render_template('index.html', postings=postings)

import sqlite3
import datetime
import sys
import logging

from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort

# global variable to get number of connections
n_connections = 0 

# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    global n_connections
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    n_connections+=1
    return connection

# Function to get a post using its ID
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    connection.close()
    return post

# Define the Flask application
app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your secret key'
logging.basicConfig(level=logging.DEBUG)

# Define the main route of the web application 
@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

# Define how each individual article is rendered 
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
      app.logger.info(str(datetime.datetime.now()) + " Page doesn't exist, 404 returned")
      return render_template('404.html'), 404
    else:
      app.logger.info(str(datetime.datetime.now())+ ' , Article "' + post['title'] + '" retrieved!')
      return render_template('post.html', post=post)

# Define the About Us page
@app.route('/about')
def about():
    app.logger.debug(str(datetime.datetime.now()) + " About Us page retrieved!")
    # print("About Us page retrieved!", file=sys.stderr)
    # print("About Us page retrieved!", file=sys.stdout)
    return render_template('about.html')

# Define the post creation functionality 
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            connection.commit()
            connection.close()
            app.logger.info(str(datetime.datetime.now()) + " " + title)
            return redirect(url_for('index'))
    return render_template('create.html')

# Define the HealthCheckpoint
@app.route('/healthz')
def healthz():
    response = app.response_class(
        response=json.dumps({"result":"OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/metrics') 
def metrics():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    response = app.response_class(
        response = json.dumps({'db_connection_count': n_connections, 'post_count': len(posts)}),
        status=200,
        mimetype='application/json'
    )
    return response


# start the application on port 3111
if __name__ == "__main__":
   app.run(host='0.0.0.0', port='3111')

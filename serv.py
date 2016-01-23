from __future__ import with_statement
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

#configuration
DATABASE = '/tmp/popol.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'smilu97'
PASSWORD = 'smilu9791'

#create our little application 
app = Flask(__name__)
app.config.from_object(__name__)

@app.before_request
def before_request() :
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	g.db.close()

def init_db() :
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql') as f :
			db.cursor().executescript(f.read())
		db.commit()

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def main_page() :
	return render_template('main_page.html')

@app.route('/<type>')
def post_page(type) :
	cur = g.db.execute('SELECT title, content, id FROM %s_posts order by id desc' % type)
	posts = [dict(title=row[0], content=row[1], id=row[2]) for row in cur.fetchall()]
	return render_template('post_page.html', posts=posts, post_type=type)

@app.route('/<type>/new')
def post_page_newpost(type) :
	return render_template('post_page_newpost.html', post_type=type)

@app.route('/<type>/<postid>')
def post_page_showpost(type, postid) :
	cur = g.db.execute('SELECT title, content, id FROM %s_posts WHERE id=%s' % (type,postid))
	posts = [dict(title=row[0], content=row[1], id=row[2]) for row in cur.fetchall()]
	return render_template('post_page_showpost.html', post=posts[0], post_type=type);

@app.route('/<type>/<int:postid>/delete')
def post_page_deletepost(type, postid):
	g.db.execute( 'DELETE FROM piano_posts WHERE id=%d'%postid)
	return redirect(url_for('piano_page'))

@app.route('/new_post', methods=['POST'])
def new_post() :
	g.db.execute('INSERT INTO %s_posts (title, content) values (?, ?)' % request.form['type'], [request.form['title'], request.form['content']])
	g.db.commit()
	return redirect('/%s'%request.form['type'])

if __name__ == '__main__' :
	app.run(host='0.0.0.0')

from flask import Flask,jsonify,url_for,render_template,redirect,request,jsonify,json
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,Resource
from flask_migrate import Migrate
from datetime import datetime
from forms import GetForm,PostForm
import os
import click

app = Flask(__name__)
db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app,db)

database_url = 'mysql+pymysql://root:fuermosi159@localhost:3306/kaihang'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret string')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', database_url)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.shell_context_processor
def make_shell_context():
	return dict(db=db,Admin=Admin,User=User,To_do_list=To_do_list)

@app.cli.command()
def initdb():
	db.create_all()
	click.echo('Initialized database')

@app.route('/')
def index():	
	return 'hello!'

@app.route('/post')
def postItem():
	return render_template('postItem.html')

class Admin(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	admin_name = db.Column(db.String(20))
	users = db.relationship('User')

class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(20))
	password = db.Column(db.String(20))
	admin_id = db.Column(db.Integer,db.ForeignKey('admin.id'))
	to_do_lists = db.relationship('To_do_list')

class To_do_list(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	item = db.Column(db.String(20))
	remark = db.Column(db.String(70))
	priority = db.Column(db.Integer)
	create_time = db.Column(db.DateTime,default=datetime.now)
	deadline = db.Column(db.DateTime)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))



class Todolist(Resource):
	def get(self):
		todo_list = []
		todolists = To_do_list.query.all()
		n = len(todolists)
		for i in range(n):
			d = dict(
					item=todolists[i].item,
					remark=todolists[i].remark,
					priority=todolists[i].priority
				)
			todo_list.append(d)
		return jsonify(todo_list)

	def post(self):
		item = request.form['item']
		remark = request.form['remark']
		priority = request.form['priority']
		to_do_list = To_do_list(item=item,remark=remark,priority=priority)
		db.session.add(to_do_list)
		db.session.commit()
		return redirect(url_for('index'))

	def delete(self):
		pass

class Todo(Resource):
	def get(self,id):
		todo_list = []
		todolist = To_do_list.query.get(id)
		d = dict(
				item = todolist.item,
				remark = todolist.remark,
				priority = todolist.priority
			)
		todo_list.append(d)
		return jsonify(todo_list)

	def put(self,id):
		pass

	def delete(self,id):
		pass

api.add_resource(Todolist,'/v1_to_do_list/')
api.add_resource(Todo,'/v1_to_do_list/<int:id>')

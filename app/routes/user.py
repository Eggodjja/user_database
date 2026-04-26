from flask import Blueprint, render_template, request, redirect
from ..extensions import db, csrf
from ..models.user import User

user = Blueprint('user', __name__)

@user.route('/', methods=['POST', 'GET'])
def all():
    users = User.query.all()
    return render_template('user/all.html', users=users)

@user.route('/user/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        user = User(first_name=first_name, last_name=last_name, email=email)
        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/')  
        except Exception as e:
            print(str(e))
            return "Something went wrong!"
    return render_template('user/create.html')

@user.route('/user/<int:id>/update', methods=['POST', 'GET'])
def update(id):
   user = User.query.get(id)
   if request.form.get('_method') == 'PUT':
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.email = request.form['email']
        try:
            db.session.commit()
            return redirect('/')  
        except Exception as e:
            print(str(e))
            return "Something went wrong!"
   return render_template('user/update.html', user=user) 

@user.route('/user/<int:id>/delete', methods=['POST', 'GET'])
def delete(id):
   if request.form.get('_method') == 'DELETE':
        user = User.query.get(id)
        try:
                db.session.delete(user)
                db.session.commit()
                return redirect('/')  
        except Exception as e:
                print(str(e))
                return "Something went wrong!"

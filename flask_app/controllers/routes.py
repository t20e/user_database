from flask import render_template, redirect, request,session
from flask_app import app
from flask_app.models.user import User
# this foler is for all the @routes 





@app.route('/')
def home():
    users = User.show_users()
    return render_template('index.html', users = users)

@app.route('/create_user')
def create_user():
    return render_template('create_user.html')

@app.route('/profile/<int:user_id>')
def profile(user_id):
    data = {
        "user_id" : user_id
    }
    user = User.profile(data)
    return render_template('profile.html', user = user)




@app.route('/created_user', methods=['GET','POST'])
def complete():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    new_user = User.add_user(data)
    return redirect('/')


@app.route('/delete/<int:user_id>', methods=['GET','POST'])
def delete_user(user_id):
    data = {
        "user_id" : user_id
    }
    delete_user = User.delete_user(data)
    print('DELETE', user_id)
    return redirect('/')

@app.route('/edit/<int:user_id>')
def edit(user_id):
    session['user'] = user_id
    users = User.show_users()
    for user in users:
        if(user_id == user.id):
            user_main = user
            print(user_main.first_name)
    print(session['user'],'***************************************')
    print('edit')
    return render_template('edit_profile.html', user_main = user_main)


@app.route('/update_user', methods= ['GET','POST'])
def update():
    # this run to update ?
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'id' :  session['user']
    }
    num = ""
    num += str(session['user'])
    print(num,'*****************')
    update_user = User.update_user(data)
    print(data)
    return redirect("/")




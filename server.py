from flask import Flask, render_template, request, redirect, jsonify
from mysqlconnection import connectToMySQL
from form import registrationForm, userUpdateForm

app = Flask('__name__')
app.secret_key = "development_tool"

@app.route("/")
@app.route("/users")
def homePage():
    my_sql = connectToMySQL('flask_pets')
    query = "SELECT * FROM users"
    usersList = my_sql.query_db(query)
    return render_template("index.html", usersList=usersList)

@app.route("/get_user_registration_form")
def get_user_registration_form():
    form = registrationForm()
    return render_template("registration_form.html", form=form)

@app.route("/save_user", methods=['POST'])
def save_users():
    my_sql = connectToMySQL('flask_pets')  
    query = "INSERT INTO users(first_name, last_name, email, create_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, NOW())"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    print(data)
    user_id = my_sql.query_db(query, data)
    print(user_id)
    return redirect("/")

@app.route("/show_user/<user_id>", methods=['GET'])
def show_user(user_id):   
    my_sql = connectToMySQL('flask_pets')    
    query = "SELECT * FROM users WHERE id = %(user_id)s"
    data = {
        "user_id": int(user_id)
    }
    user = my_sql.query_db(query, data)
    print(user)
    return render_template("user_info.html", user=user)

@app.route("/get_user_update_form/<user_id>", methods=['GET'])
def get_user_update_form(user_id):
    form = userUpdateForm()
    my_sql = connectToMySQL('flask_pets')    
    query = "SELECT * FROM users WHERE id = %(user_id)s"
    data = {
        "user_id": int(user_id)
    }
    user = my_sql.query_db(query, data)
    print(user)
    return render_template("update_form.html", user=user, form=form)

@app.route("/update_user/<user_id>", methods=['POST'])
def update_user(user_id):
    my_sql = connectToMySQL('flask_pets')    
    query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, update_at = NOW() WHERE id = %(user_id)s"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "user_id": int(user_id)
    }
    user = my_sql.query_db(query, data)
    print(user)
    return redirect("/")

@app.route("/delete_user/<user_id>", methods=['GET'])
def delete_user(user_id):
    my_sql = connectToMySQL('flask_pets')    
    query = "DELETE FROM users WHERE id = %(user_id)s"
    data = {        
        "user_id": int(user_id)
    }
    user = my_sql.query_db(query, data)
    print(user)
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
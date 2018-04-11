from flask import Flask, redirect, render_template, request
# import the function connectToMySQL from the file mysqlconnection.pycopy
from mysqlconnection import connectToMySQL

app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('myfriends')
# now, we may invoke the query_db method

@app.route('/')
def index():
    all_friends = mysql.query_db("SELECT * FROM friends")

    print("Fetched all friends", all_friends)

    return render_template('index.html', friends = all_friends)


@app.route('/add', methods=['POST'])
def addFriend():
    query = "INSERT INTO friends (name, age, created_at, updated_at) VALUES (%(name)s, %(age)s, NOW(), NOW());"
    data = {
             'name': request.form['name'],
             'age':  request.form['age']
           }
    mysql.query_db(query, data)

    return redirect('/')

print("all the users", mysql.query_db("SELECT * FROM friends;"))
if __name__ == "__main__":
    app.run(debug=True)
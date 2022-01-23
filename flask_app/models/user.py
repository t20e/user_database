from flask_app.config.mysqlconnection import connectToMySQL
# this folder is for all classes models that we are controlling

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def show_users(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('users_schema').query_db(query)
        print(results)
        users = []
        for user_data in results:
            users.append(cls(user_data))
        print(users)
        return users

    @classmethod
    def add_user(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW() ) "
        results = connectToMySQL('users_schema').query_db(query,data)
        print(results)
        return results

    @classmethod
    def profile(cls,data):
        query = "SELECT * FROM users WHERE id = %(user_id)s "
        results = connectToMySQL('users_schema').query_db(query,data)
        print(results)
        return cls(results[0])

    @classmethod
    def delete_user(cls,data):
        query = "DELETE FROM users WHERE id = %(user_id)s "
        results = connectToMySQL('users_schema').query_db(query,data)
        print(results)
        return cls

    @classmethod
    def update_user(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s"
        results = connectToMySQL('users_schema').query_db(query,data)
        print(results)
        return cls
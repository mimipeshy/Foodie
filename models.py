import auth
import datetime
import os
import jwt
from werkzeug.security  import generate_password_hash, check_password_hash

orders = {}
users = {}
order_id = 1


def invalid_email():
    return {"invalid email"}


class Users:
    """contains methods for user class"""

    def create_new_user (self, email, username, password, is_admin= False):
        """this creates a new user"""
        hashed_password = generate_password_hash(password, method='sha256')
        users[email] = {"username": username,
                        "password": hashed_password,
                        "is_admin": is_admin
                        }
        return {"User has been created"}

    def user_login(self, email, password):
        """this logs in a registered user"""
        if email in users:
            if generate_password_hash(users['email']['password'], password):
                user_email= email
                admin = users[email]['is_admin']
                token= jwt.encode ({'email':user_email,'is_admin':admin,
                                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=20)},
                                   os.getenv('SECRET_KEY'))
                return {'token': token.decode('UTF-8')}
            else:
                return  {"passwords do not match"}, 401
        else:
            return  {"Invalid email"}, 401


    def get_all_users(self):
        """gets all users"""
        return users

    def get_one_user(self, email):
        """gets one user"""
        if email not in users:
            return invalid_email()
        else:
            response = users.get(email)
            return response

    def delete_one_user(self, email):
        """deletes a single user"""
        if email not in users:
            return invalid_email()
        else:
            del users[email]
            return {'User deleted successfully'}

    def promote_user (self, email):
        """makes a user an admin"""
        if email not in users:
            return invalid_email()
        else:
            user= users.get(email)
            user ['is_admin'] = True
            return {"User is now an admin"}

    def modify_username (self, email, username):
        """user can update their usernames"""
        if email not in users:
            return invalid_email()
        user = users.get(email)
        user['username'] = username
        return {"Username successfully updated"}

    def reset_password (self, email, password):
        if email not in users:
            return invalid_email()
        user = users.get(password)
        hashed_password = generate_password_hash(password, method='sha256')
        user ['password']= hashed_password
        return {"Password has been reset successfully"}

def invalid_order():
    return {"Invalid Order"}


class Orders:
    """contains all methods for order class"""

    def get_all_orders(self):
        """returns orders"""

        output = []
        for order_id in orders:
            data = {}
            data["order_id"] = order_id
            data["order_type"] = orders[order_id]["order_type"]
            data["quantity"] = orders[order_id]["quantity"]
            data["customer_name"] = orders[order_id]["customer_name"]
            data["price"] = orders[order_id]["price"]
            output.append(data)
        return output

    def get_one_order(self, order_id):
        """this gets one particular order details"""
        if order_id not in orders:
            return invalid_order()

        order = orders.get(order_id)
        return order

    @staticmethod
    def place_order(order_type, quantity, price, customer_name, status=False):
        """places a new order"""
        global orders
        global order_id
        orders[order_id] = {"id": order_id,
                            "order_type": order_type,
                            "quantity": quantity,
                            "price": price,
                            "customer_name": customer_name,
                            "status": status
                            }
        new_order = orders[order_id]
        order_id += 1
        return new_order

    def update_an_order(self, order_id):
        """this updates an order"""
        if order_id not in orders:
            return invalid_order()

        order = orders.get(order_id)

        order['status'] = True
        return {"msg": 'order is approved!'}

    def delete_an_order (self, order_id):
        """this deletes an order"""
        if orders not in orders:
            return invalid_email()
        del orders [order_id]
        return {"Order deleted successfully"}

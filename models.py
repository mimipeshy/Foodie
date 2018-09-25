import auth
import datetime
import os
import jwt
from werkzeug.security  import generate_password_hash, check_password_hash

orders = {}
order_id = 1

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

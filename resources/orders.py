from flask_restplus import Namespace, Resource, reqparse, fields
from models import Orders

orders = Orders()
api = Namespace("Orders", description="Order related operations")
request_model = api.model('Request Model', {"order_type": fields.String,
                                            "quantity": fields.Integer,
                                            "customer_name":fields.String,
                                            "price": fields.Integer})


class OrderList(Resource):
    """Contains GET methods"""

    def get(self):
        """Gets a list of all orders"""
        response = Orders.get_all_orders(self)
        return response, 200

    @api.expect(request_model)
    def post(self):
        """Place a new order for food"""
        parser = reqparse.RequestParser()

        parser.add_argument('order_type', required=True, type=str, help='Order type is required', location=['json'])
        parser.add_argument('quantity', required=True, type=str, help='Please input a quantity', location=['json'])
        parser.add_argument('customer_name', required= True, type= str, help= 'Input customer name', location=['json'])
        parser.add_argument('price', required=True, type=int, help='Please input a price', location=['json'])

        args = parser.parse_args()
        result = Orders.place_order(order_type=args['order_type'], quantity=args['quantity'],customer_name=args['customer_name'],
                                    price=args['price'])
        return result, 201


class Order(Resource):
    """contains GET and PUT endpoints"""

    def get(self, order_id):
        """Fetch a specific order"""
        response = Orders.get_one_order(self, order_id= order_id)
        return response, 200

    def put(self, order_id):
        """updates the order status"""
        response = Orders.update_an_order(self,order_id= order_id)
        return response, 200


api.add_resource(OrderList, '/orders', endpoint='orderlist')
api.add_resource(Order, '/orders/<int:order_id>/')

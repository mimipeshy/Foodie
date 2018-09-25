import unittest
import sys  # fix import errors
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tests.base_test import BaseTests


class OrdersEndpoint(BaseTests):
    """This class represents order test cases"""

    def test_add_order(self):
        """test api can add order"""
        order = {"order_type": "fish and chips", "quantity": "one", "price": "300", "customer_name": "peshy"}
        res = self.client().post('/api/v1/orders', data=json.dumps(order), content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_get_one_order(self):
        """test api can get one specific order"""
        order = {"order_id": "1"}
        res = self.client().get('api/v1/orders/1', data=json.dumps(order),
                                content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_get_all_orders(self):
        """tests that api can fetch all orders"""
        order = {"order_type": "fish and chips", "quantity": "one", "price": "300", "customer_name": "peshy"}
        res = self.client().get('/api/v1/orders', data=json.dumps(order), content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_update_an_order(self):
        """tests that api can update an order"""
        order = {"order_type": "fish and chips", "quantity": "one", "price": "300", "customer_name": "peshy"}
        res = self.client().put('/api/v1/orders/1', data=json.dumps(order), content_type='application/json')
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()

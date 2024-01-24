import random
import uuid

from jafgen.customers.order_item import OrderItem
from jafgen.customers.payment import Payment


class Order(object):
    _id_counter = 1

    def __init__(self, customer, items, store, day):
        self.order_id = Order._get_next_id()
        self.customer = customer
        self.items = [OrderItem(self.order_id, item) for item in items]
        self.payments = Order._get_payments(self.order_id)
        self.store = store
        self.day = day
        self.subtotal = sum(i.item.price for i in self.items)
        self.tax_paid = store.tax_rate * self.subtotal
        self.order_total = self.subtotal + self.tax_paid
        self.status = Order._get_status()

    @classmethod
    def _get_next_id(cls):
        current_id = cls._id_counter
        cls._id_counter += 1
        return current_id

    @classmethod
    def _get_status(cls):
        return random.choices(['completed', 'shipped', 'placed', 'returned', 'return_pending'], weights=[67, 13, 13, 4, 2])[0]

    @classmethod
    def _get_payments(self, order_id):
        payments = [Payment(order_id)]
        while random.random() < 0.15:
            payment = Payment(order_id)
            payments.append(payment)
        return payments

    def __str__(self):
        return f"{self.customer.first_name}  {self.customer.last_name}bought {str(self.items)} at {self.day}"

    def to_dict(self):
        return {
            "id": self.order_id,
            "user_id": self.customer.customer_id,
            # "ordered_at": self.day.date.isoformat(),
            # "order_month": self.day.date.strftime("%Y-%m"),
            'order_date': self.day.date.strftime("%Y-%m-%d"),
            # "store_id": self.store.store_id,
            # "subtotal": int(self.subtotal * 100),
            # "tax_paid": int(self.tax_paid * 100),
            # "order_total": int(self.order_total * 100),
            'status': self.status,
        }

    def items_to_dict(self):
        return [i.to_dict(self.order_id) for i in self.items]

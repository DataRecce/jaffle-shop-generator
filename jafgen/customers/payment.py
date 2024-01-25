import uuid
import random


class Payment(object):
    _id_counter = 1

    def __init__(self, order_id):
        self.id = Payment._get_next_id()
        self.order_id = order_id
        self.payment_method = Payment._get_payment_method()
        self.amount = random.randint(1, 30) * 100

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            'payment_method': self.payment_method,
            'amount': self.amount,
        }

    @classmethod
    def _get_next_id(cls):
        current_id = cls._id_counter
        cls._id_counter += 1
        return current_id

    @classmethod
    def _get_payment_method(cls):
        return random.choices(
            ['credit_card', 'bank_transfer', 'coupon', 'gift_card'],
            weights=[55, 33, 13, 12]
        )[0]

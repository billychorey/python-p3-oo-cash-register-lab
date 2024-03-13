class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction.append(
            {'title': title, 'price': price, 'quantity': quantity}
        ) 
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total = round(self.total - discount_amount)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print('There is no discount to apply.')

    def void_last_transaction(self):
        if not self.last_transaction:
            print("No transactions to void.")
        else:
            self.total -= (
                self.last_transaction[-1]['price'] * self.last_transaction[-1]['quantity']
            )
            # self.items.pop()  # Remove the last item from the list
            for _ in range(self.last_transaction[-1]['quantity']):
                self.items.pop()
            self.last_transaction.pop()

    def price_of_item(self, item):
        return 0

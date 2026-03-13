# Create a closure that remembers the discount percentage.

def discount(percent):
    def discount_amount(price):
        discount_price = price * percent / 100
        return price - discount_price
    return discount_amount

calculate_discount = discount(10)
print(calculate_discount(100))
print(calculate_discount(200))
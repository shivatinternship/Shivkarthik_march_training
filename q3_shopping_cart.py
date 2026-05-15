# PART A
def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", ["bread"]))
print(add_item("eggs"))

# Output:
# ['apple']
# ['apple', 'banana']
# ['bread', 'milk']
# ['apple', 'banana', 'eggs']

#Explanation:
# The default list cart=[] is created only once.
# So every time the function is called without passing a cart,
# the same list is reused and keeps getting modified.

# First call:
# ['apple']

# Second call uses the same list:
# ['apple', 'banana']

# Third call passes a new list manually:
# ['bread', 'milk']

# Fourth call again uses the original shared list:
# ['apple', 'banana', 'eggs']

# This happens because lists are mutable.

# PART B
def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print("\nCorrect Version")
print(add_item_fixed("apple"))
print(add_item_fixed("banana"))
print(add_item_fixed("eggs"))


# PART C
def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }

def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({
        "name": name,
        "price": price,
        "qty": qty
    })

def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError:
        print("Tuples are immutable")

def calculate_total(cart):
    total = 0
    for item in cart["items"]:
        total += item["price"] * item["qty"]
    discount_amount = total * (cart["discount"] / 100)
    return total - discount_amount

cart1 = create_cart("Shiv", 10)
cart2 = create_cart("Rahul", 5)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 1000, 2)

add_to_cart(cart2, "Phone", 25000, 1)
add_to_cart(cart2, "Charger", 1500, 1)

print("\nCart 1:", cart1)
print("Cart 2:", cart2)
print("\nFinal Total for Cart 1:", calculate_total(cart1))
print("Final Total for Cart 2:", calculate_total(cart2))

price_tuple = (500, 600)
update_price(price_tuple, 700)

# Discussion Points
# 1. discount=0 is safe because int is immutable.
#    cart=[] is dangerous because list is mutable.

# 2. Rebinding means assigning a new object.
#    Mutating means changing the existing object.

# 3. Mutable -> list, dict, set
#    Immutable -> tuple, str, int

# 4. Yes, changes reflect outside because lists are mutable.

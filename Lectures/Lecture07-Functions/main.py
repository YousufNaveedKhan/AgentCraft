# Yahan function define krrhe hain ( without parameter )
def say_hello():
    # docString
    """Yeh hello print krega"""
    print("HELLO")

# Function Call / Calling
say_hello()

# Function with parameter
def greet(name, greeting="Hello"): 
    print(f"{greeting}, {name}")

greet("Sufiyan")
greet("Sufiyan", "Welcome")


def is_adult(user):
    """User ki age agar 18 ya ussay zyada hogi tou yeh True return krega"""
    return user["age"] >= 18

def summarize_users(users):
    """Users ki age dekhte huwe adults or minors ka count btadega"""
    adults = 0
    minors = 0

    for user in users:
        if is_adult(user):
            adults += 1
        else: 
            minors += 1
    print(f"Adults: {adults}, Minors: {minors}")

users = [
    {"name": "Shayan", "age": 18},
    {"name": "Sufyan", "age": 14},
    {"name": "Aaqib", "age": 20},
    {"name": "Ayaan", "age": 17},
    {"name": "Hashim", "age": 16},
]

summarize_users(users)

def get_percentage(obtained, total):
    try:
        return obtained / total * 100
    except ZeroDivisionError: 
        print("Total marks zero nahin hosakte!")
        return None

print(get_percentage(85, 100))
print(get_percentage(85, 0))

def add_number(*args):
    return sum(args)

print(add_number(2,4,6,7))
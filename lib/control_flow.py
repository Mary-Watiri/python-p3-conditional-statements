#!/usr/bin/env python3


   
def admin_login(username, password):
    if username.upper() == "ADMIN" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
print(admin_login("admin", "12345"))
print(admin_login("ADMIN", "12345"))
print(admin_login("adminn", "12345"))

def hows_the_weather(temp):
    if temp < 40:
        return "It's brisk out there!"
    elif 40 <= temp <= 65:
        return "It's a little chilly out there!"
    elif temp > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

hows_the_weather(55)
hows_the_weather(99)
hows_the_weather(75)
hows_the_weather(33)


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

fizzbuzz(0)
fizzbuzz(15)
fizzbuzz(45)
fizzbuzz(3)
fizzbuzz(33)
fizzbuzz(42)
fizzbuzz(5)
fizzbuzz(10)
fizzbuzz(50)
fizzbuzz(2)
fizzbuzz(13)
fizzbuzz(59)

def calculator(operation, x, y):
    dict_map = {
        "+": x + y, 
        "-": x - y,
        "*": x * y,
        "/": x / y,
    }
   
    result = dict_map.get(operation)
    if result is None:
        print("Invalid operation!")
        return None
    else:
        return result
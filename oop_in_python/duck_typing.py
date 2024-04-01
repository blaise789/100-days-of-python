# # # Duck typing where the class of an object is less important than the methods class type is not checked if minimum methods/ attributes are present "if it walks like a duck ,and it quacks like a duck the it must be a duck
# # class Duck:
# #     def walk(self):
# #         print("this duck is walking")
# #
# #     def talk(self):
# #         print("this duck is quacking")
# #
# #
# # class Chicken:
# #     def walk(self):
# #         print("this chicken is walking")
# #
# #     def talk(self):
# #         print("this chicken is clucking")
# #
# #
# # class Person:
# #     def catch(self, duck):
# #         duck.walk()
# #         duck.talk()
# #         print("You caught the critter!")
# #
# #
# # duck = Duck()
# # chicken = Chicken()
# # person = Person()
# # person.catch(chicken)
#
# # walrus operator
# # print(happy := True)
#
# # foods = list()
# # while True:
# #     print(len(foods))
# #     food = input("what food do you like?:")
# #     foods.append(food)
# #     choice = input("would you like to enter more (Yes,No)").lower()
# #     if choice == 'no':
# #         break
# # using walrus operator
# # foods = list()
# # while choice := input("would you like to enter the food you like (Yes,No)? ").lower() != "No":
# #     food = input("what food do you like?:")
# #     foods.append(food)
#
# def hello():
#     print("hello")
#
# say = print
# say("hey bro")
# hi = hello
# hi()
# high order functions accepts functions as arguments or returns functions
# functions are treated as objects
def loud(text):
    return text.upper()


# def quiet(text):
#     return text.lower()
#
#
# def hello(func):
#     text = func("hello")
#     print(text)
#
#
# hello(loud)
# def divisor(x):
#     def dividend(y):
#         return y / x
#
#     return dividend


# divide = divisor(2)
# print(divide(10))
# lambda functions  = functions written in 1 line using lambda keyword
# accepts any number of arguments, but only has one expression
# think of it as a shortcut (useful if needed for a short period of time, throw-away)
# # lambda  parameters:expression
# def double(x):
#     return x *2
# double = lambda x: x * 2
# # age_check=lambda  age:True if age>18  else False;
# age_check=lambda  age:True if age>18 else False
# print(double(5))
# students=["blaise","sammy","elite","pacifique"]
# students.sort()
# # sort methods works only on list
# for i in students:
#     print(i)
#

# sorted function for iterables
# students=("blaise","sammy","elite","pacifique")
# sorted_students=sorted(students)
# for i in sorted_students:
# #     print(i)
# students=[("blaise","D"),("sammy","A"),("elite","C"),("pacifique","B")]
# grades=lambda data:data[1]
# # students.sort(key=grades,reverse=True)
# sorted(students,key=grades)
# for i in students:
#     print(i)

# map function
# #  applies a function to each item in an iterable(list,tuple,etc)
# store = [("shirt", 20.00),
#          ("pants", 25.00),
#          ("jacket", 50.00),
#          ("socks", 10.00),
#          # "money"
#          ]
#
# to_euros = lambda data: (data[0], data[1] * 0.82)
# stores_euros = list(map(to_euros, store))
# for item in stores_euros:
#     print(item)
# #     filter function  creates a  collection of elements from an iterable for which a function returns
#
# friends = [
#     ("Elite", 19),
#     ("Paccy", 20),
#     ("Sammy", 18),
#     ("Someone", 17)
# ]
# age_filter = lambda data:  data[1]>= 18
# friends_filtered = list(filter(age_filter, friends))
# for i in friends_filtered:
#     print(i)
# # reduce function
import functools as func

# letters = ["H", "E", "L", "L", "O"]
#
# word = func.reduce(lambda x, y: x + y, letters)
# print(word)
# factorial = [5, 4, 3, 2, 1]
# fact = func.reduce(lambda x, y: x * y, factorial)
# print(fact)
# student_marks = [100, 90, 80, 70, 60, 50, 30, 20, 10]
# filtered_marks=filter(lambda x:x>=60,student_marks)
# for  x in filtered_marks:
#     print(x)
# list comprehension
# format is [expression  for loop in  iterable
# list_comprehended = [x if x >= 60 else "Failed" for x in student_marks]
# for i in list_comprehended:
    # print(i)
# dictionary comprehension  format dict_comprehended
#  cities in farheit
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# cities_in_C = {key: ((value-32)*(5/9)) for (key, value) in cities_in_F.items()}
# print(cities_in_C)
# cities_weather_desc={city:("warm" if deg>=75 else "cold" )  for (city,deg) in cities_in_F.items()  }
# cities_weather_desc={city:("warm" if deg>=75 else "cold" )  for (city,deg) in cities_in_F.items()  }
# weather={"New York":"snowing","Boston":"sunny","los angeles":"sunny","chicago":"cloudy"}

# sunny_weather={key:value for (key,value) in weather.items() if value=="sunny"}
# print(sunny_weather)
# print(cities_weather_desc)
def check_temp(value):
    if value >= 70:
        return  "HOT"
    elif 69>=value>=40:
        return "WARM"
    else:
        return  "COLD"
cities_weather_desc={city:check_temp(deg)  for (city,deg) in cities_in_F.items()  }
print(cities_weather_desc)

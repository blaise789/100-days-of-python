# # import  time
# #
# # # website = "http://google.com"
# # # web_slice=slice(7,-4)
# # # print(website[web_slice])
# # # raise nam
# # # name=None
# # # while not name or name.isdigit():
# # #     name = input("enter your name ")
# # #
# # # print(name)
# #
# # # for seconds in range(10,0,-1):
# # #     print(seconds)
# # #     time.sleep(1)
# # # print('hey bro')
# # rows=int(input("how many rows?: "))
# # columns=int(input("how many columns?: "))
# # symbol=input("which symbol to use?:")
# # for i in range(rows):
# #     for j in range(columns):
# #         print(symbol,end="")
# #     print()
# #     def hello(first,middle,last):
# #         print("Hello"+first+" "+middle+" "+last)
# #     hello(last='kevin',middle="kubwayo",first="k")
# # print(round(abs(float(input("enter the number")))))
# # nested functions
# # def add(*args):
# #     # tuple
# #     args=list(args)
# #     args[0]=30
# #     sum=0
# #     for i in args:
# #         sum+=i;
# #     return sum
# # print(add(1,23,10))
# # dictionary
#
# def hello(**kwargs):
#     print("Hello",end=" ")
#     for key,value in kwargs.items():
#         print(value,end=" ")
# hello(title="Coder",first="Bigirabagabo",middle="patience",last="Blaise")

# animal="cow"
# item= "moon"
# name="kevin"
# print("the {} jumped over the {}".format(animal,item))
# print("the {1} jumped over {1}".format(animal,item))
# print("the {animal} jumped over the {item}".format(animal="dog",item="moon"))
# print("hello, my name is {:10}.nice to meet you".format(name))
# print("hedllo, my name is {:<10}.nice to meet you".format(name))
# print("hello, my name is {:>10}.nice to meet you".format(name))
# print("hello, my name is {:^10}.nice to meet you".format(name))
# # numbers formatting
# number=3.1423
# num2=1000
# print("the numbers formated {:.2f}".format(number))
# print("the numbers formated {:,}".format(num2))
# print("the numbers formated {:b}".format(num2))
# # print("the numbers formated {:ax}".format(num2))
# import  random
# x=random.randint(1,6)
# # dice rolling
# y=random.random()
# myList=["rock","paper","scissors"]
# z=random.choice(myList)
# print(x,y,z)
# cards=[1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
# random.shuffle(cards)
# print(cards)
# exception
# try:
#  numerator=int(input("enter a number to divide: "))
#  denominator=int(input("enter the number to divide by:"))
#  result=numerator/denominator
# except ZeroDivisionError:
#     print("you can't divide by zero! bro ")
# except ValueError as e:
#     print("enter only numbers please")
#     print(e)
# except Exception:
#     print(f"something went wrong(:")
#
#
# else:
#     print(result)
# finally:
#     print("the block above will always execute")
# import  os
# if os.path.exists(path):
#     print("that location exists")
#     if os.path.isfile(path):
#         print("that is file")
#     elif os.path.isdir(path):
#         print("that is a directory")
# else:
#     print("that location
#     does not exists")
# try:
#  with open(path) as file:
#     print(file.read())
# except FileNotFoundError:
#     print("that file was not found:(")
# # print(file.closed)

# text="Only God knows the way to do it "
# # with open('teacher.txt','w') as file:
# #     file.write(text)
# with open('teacher.txt','a') as file:
#     file.write(text)
import  shutil
path="C:\\Users\\bigirabagaboblaise\\Documents\\Academic\\test.txt"
shutil.copyfile('teacher.txt',path)

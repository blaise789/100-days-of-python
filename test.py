# import math
# x=y=z=10
# name,age,happy="Blaise",20,True
# height=float(input("what is your height?"))
# print(int(age))
# print(name*3)
# print(math.ceil(height))
# # slicing
# name="kevin madusa"
# first_name=name[::2]
# reverse_name=name[::-1]
# print(first_name)
# print(reverse_name)
# website="http://google.com"
# slice=slice(7,-4)
# print(website[slice])
# age=int(input("how old are you?"))
# # if age==100:
# #     print("you are century old ");
# # elif age>=18:
# #     print("you are an adult")
# # elif age<0:
# #     print("you haven't been born yet")
# # if 
# if not age>=18:
#     print("you are a kid buddy")
# else:
#     print("you are an adult")   
# while loop 
# name=None 
# while  not name:

#     name=input("enter your name ")
# print("hello"+name)
 
# for loop 
# multiplication table 
# import time;

# for num in range(1,13):
#     for mult in range(1,13):
#       result=mult*num;
#       print(str(num)+"*"+str(mult)+"="+str(result))
# # count down
# for seconds in range(10,0,-1):
#     print(seconds);
#     # time.sleep(1)
# print("happy new year!")   
# rows=int(input("enter how many rows?:"))
# columns=int(input("enter the number of columns?:"))
# symbol=input("enter the symbol?")
# for i in range(rows):
#     for j in range(columns):
#         print(symbol,end="")
#     print()    
        
#         # lists
# foods=["ringi","hotdog","mushrooms","rice"]
# drinks=["milk","juice","water"]
# sports=["football","basketball","tennis"]
# dinner=[foods,drinks,sports]
# print(dinner[0][1])
 

# # for x in foods:
# #     print(x)  
          
# # tuples 
# student=("Blaise",19,"male")
# for x in student:
#     print(x)
# if "Blaise" in student:
#     print ("blaise is a good student")      
#     # 
     
# # a set is a collection which is  unordered ,unindexed,No duplicate values
# utensils={"fork","knife","slicer"}
# dishes={"bowl","plate","cup","fork","slicer"}
# dinner_table=utensils.union(dishes)
# print(dishes.difference(utensils))
# for x in dinner_table:
#     print(x)
# dictionary keys and values pairs
# kwargs
# capitals={
#     "USA":"washington",
#     "Rwanda":"Kigali",
#     "China":"beijing"
# }
# # print(capitals["China"])

# # print(capitals.get('burundi'))
# capitals.update({"Burundi":"Bujumbura"})
# for key,value in capitals.items():
#     print(key+": "+value)

# print(round(abs(float(input("enter the whole positive number")))))
# def add(*numbers):
#     sum=0
#     stuff=list(numbers)
#     for x in stuff:
#         sum +=x
        
#     return sum    
# print(add(1,2,3,6))
# def hello(**kwargs):
    # print("hello"+kwargs['first']+" "+kwargs['second'])
animal="dog"
item="desk"    
print("the {1} jumped over the {0}".format(animal,item)) 
print("the {student} kicked the {teacher} ".format(student="kevin",teacher="emmy"))   
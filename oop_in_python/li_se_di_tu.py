usernames=["Madusa","Kevin","Vayi","hey"]
passwords=["Madusa@123","Kevin@123","abc23",]
# users=zip(usernames,passwords)
# users=list(zip(usernames,passwords))
# zip(*iterables ) aggregates elements from two or more iterables creates a zip object with paired elements  stored in tuples for each e
users=dict(zip(usernames,passwords))
print(users)
for (key,value) in users.items():
    print(key,value)


# for i in users:
#     print(i)
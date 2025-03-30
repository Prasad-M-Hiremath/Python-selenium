#LISTS
a= [1, 2, "prasad", 4, 5]
print(a[0])                            #1
print(a[-1])                         #5
a.insert(3, "man")   #inserted man at index 3
a.append("break")                  #appended at last
a[2]="PRASAD"                 #updated value
del a[0]                #deleted index val of 1
print(a)
print(type(a))


#TOUPLES
a = (1, 2, "john", 4, 5)
print(a)
print(type(a))


#DICTIONARIES

a = {1:"prasad", 2:"john", "age":50}
print(a)
print(type(a))
print(a["age"])
print((a[1]))
print((a[2]))



#ADDING NEW VALUE TO DICTIONARIES
dict = {}
dict["firstname"] = "Prasad"
dict["lastname"] = "Hiremath"
dict["gender"] = "Male"
dict[4] = "funny"
print(dict)
print(dict["lastname"])
print(dict["firstname"])
print(dict["gender"])
print(dict[4])
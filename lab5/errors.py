
# a=5/0  # exception errors
# print(a)  

#  try and except

# def divide(a,b):
#     return a/b

# a= int (input("enter numerator: "))
# b= int(input("enter denominator: "))

# try:
#     # value= divide(40, 10)
   
#    val = divide(a , b)
#    print(val)
# except Exception as e:
#     print("Something is wrong! -> ", e)
#     print(e.__class__)



try:
    items=[1,2,3,4,5]
    item= items[6]
    # item= items[2]
    print(item)
except:
    print("Something is wrong")

myGlobal =10

def fn1():
  enclosedV = 8

  def fn2():
    localV= 5
    print('Access to global', myGlobal)
    print('Access to encloases', enclosedV)


# print(localV)
# print(enclosedV)
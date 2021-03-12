#def subtract(*num):
#    a= 100
#    for number in num:
#        a-= number
#    return a
#print(subtract(1,10,20,13,37))

#def func1(x): return x**2
#def func2(x): return x
#for x in list(range(3)):
#    print((lambda x: func1(x)*func2(x))(x), end=" ")

#string = input()
#if (string == string.upper()):
#    print(True)
#else:
#    print(False)

#randomStr= "This is a custom string to be manipulated."
#randomStr.replace('i', "", 10)
#print(randomStr)

#def randomFunc(x,y,z):
#    x = y+z
#    y = x+z
#    z = x+y
#    return x,y,z
#a,b,c = randomFunc(y=5, z=3, x=6)
#print(a,b,c)

#def random():
#    count=0
#    for i in [i for i in range(0,10)]:
#        count +=1
#    return count
#print(random())

#def main(customInp):
#    try:
#        print(customInp + 1)
#    except TypeError:
#        print(int(customInp) + 2)
#    finally:
#        return "Done."
#if __name__ == "__main__":
#    customInp = input()
#    print(main(customInp))

#print({random**2 for random in range (10)})

#x = 15.0
#y = 0.0
#def main (x,y):
#    try:
#        return x/y
#    except ZeroDivisionError:
#        return x/1
#print(main(x,y))

#def main(*args):
#    toBeDivided = 100
#
#    for i in args:
#        try:
#            toBeDivided /= i
#        except ZeroDivisionError:
#            print("You can not divide by 0!", end=" ")
#    return toBeDivided
#print (main(1,2,0,5))
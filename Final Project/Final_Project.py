r=0
w=0
print ("Welcome to Knowledge Competition!!!")
print ("Answer the following questions!")
print ("Q1: What is the command that returns the number of items from a sequence or characters in a string?")
A1 = input("Enter your answer: ").lower
if A1 == "len":
    r+=1
else:
    w+=1
print ("Q2: Which command converts a string to an integer?")
A2 = input("Enter your answer: ").lower
if A2 == "int":
    r+=1
else:
    w+=1
print ("Q3: Which method splits a string into separate phrases?")
A3 = input("Enter your answer: ").lower
if A3 == "split":
    r+=1
else:
    w+=1
print ("Q4: Which method sorts a list from smallest to highest or a string alphabetically?")
A4 = input("Enter your answer: ").lower
if A4 == "sorted":
    r+=1
else:
    w+=1
print ("Q5: What is '!='?")
A5 = input("Enter your answer: ").lower
if A5 == "not equal":
    r+=1
else:
    w+=1
print ("Q6: Which method adds input to the end of a list?")
A6 = input("Enter your answer: ").lower
if A6 == "append":
    r+=1
else:
    w+=1
print ("Q7: Which command converts a string to uppercase?")
A7 = input("Enter your answer: ").lower
if A7 == "upper":
    r+=1
else:
    w+=1
print ("Q8: Which command interrupt the (loop) cycle?")
A8 = input("Enter your answer: ").lower
if A8 == "break":
    r+=1
else:
    w+=1
print ("Q9: Which command exits the function and returns a value?")
A9 = input("Enter your answer: ").lower
if A9 == "return":
    r+=1
else:
    w+=1
print ("Q10: What creates a new anonymous function?")
A10 = input("Enter your answer: ").lower
if A10 == "lambda":
    r+=1
else:
    w+=1

print("Your competition has finished.\n\n")

if r > 5:
    print(f"{r} questions are correct. You are successful")
else:
    print(f"{w} questions are false. You are unsuccessful")










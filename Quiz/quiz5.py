#import numpy as np
#transpose_a = np.array([[20,15,20,29,13]
#                        [14,5,19,7,10]
#                        [6,24,26,13,28]])
#print(transpose_a.T)

#customTup = (4,3,2,1,0)
#customLst = [0,1,2,3,4]
#def main(customTup, customLst):
#    if customTup.index(2) == customLst[-3]:
#        return True
#    else:
#        return False
#print(main(customTup, customLst))

#array([[[[1,2,3],
#         [4,5,6],
#         [7,8,9]]]])

#b = np.array([[1,2,3,4],
#              [5,6,7,8]])
#b.ravel()

#a = np.array([9,10])
#b = np.array([11,12])
#print(np.dot(a,b))

#import numpy as np
#d=np.array([[1,2,3],
#            [4,5,6],
#            [7,8,9]])
#print(d.shape)

#rawInp = "12345"
#def main(rawInp):
#    revStr = ""
#    for i in range(len(rawInp)):
#        revStr += rawInp[1-i]
#    if revStr == rawInp[::-1]:
#        return rawInp[::-1]
#    else:
#        return revStr
#print(main(rawInp))

#rawInp1 = "123"
#rawInp2 = "1"
#try:
#    print(lent(rawInp1) / len(rawInp2), end=" ")
#except:
#    print("Can not.", end =" ")
#finally:
#    print("Done")

#X = [[1,8,3],
#     [6,5,4],
#     [7,2,9]]
#Y = [[9,2,9],
#     [4,5,6],
#     [5,10,5]]
#res = [[0,0,0],
#     [0,0,0],
#     [0,0,0]]
#for i in range (len(X)):
#    for j in range(len(X[0])):
#        res[i][j] = X[i][j] + Y[i][j]
#for r in res:
#    print(r, end=" ")

#import pandas as pd
#employees = pd.DataFrame({
#    "Name": ["John", "Doe", "William", "Spark", "Mark"],
#    "Occupation": ["Chemist", "Teacher", "Statistician", "Scientist", "Developer"],
#    "Age": [23,24,34,29,40]})
#employees.drop("Age", axis=1, inplace=True)
#print(employees)
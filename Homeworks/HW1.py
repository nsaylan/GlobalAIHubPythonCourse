odd = [1, 3, 5, 7, 9]
even = [0, 2, 4, 6, 8]
oddm = []
evenm = []
for i in odd:
    oddm.append(i*2)
for i in even:
    evenm.append(i*2)
for a in zip (oddm,evenm):
    print(a)
    print(type(a))
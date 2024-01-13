myData = '''
n = int(input("Your Number"))
if n == 1:
    print(True)
elif n == 2:
    print(False)
'''

Flag = True
Final = 2147483647
for i in range(3, Final):
    if Flag:
        myData += f'''
elif n == {i}:
    print(True)'''
        Flag = False
    else:
        myData += f'''
elif n == {i}:
    print(False)'''
        Flag = True

f = open("isOdd.py","w")
f.write(myData)
f.close()

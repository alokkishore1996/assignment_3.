def fun (str):
    n1 = 0
    n2 = 0
    for i in str:
       if i.islower():
        n1 = n1 + 1
       elif i.isupper():
        n2 = n2 + 1
    print("lower case letters:",n1)
    print("upper case letters:",n2)
fun("The quick Brow Fox")

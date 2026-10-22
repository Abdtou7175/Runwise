print("Hello world!")
print("This is a test commit")
print("Hello world!")

l = [5,12,2,98,43,12,65,0,1,5,6,7,8,9]
swap = True
while swap:
    swap = False
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            swap = True
    print(l)

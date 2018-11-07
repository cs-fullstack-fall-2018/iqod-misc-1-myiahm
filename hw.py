arr = [1,2,200,156,100]

arr.sort()
print 'The min number in the array is ', arr[0] , 'and the max is ', arr[4]




#if u wanted a blank array that the user could add to and it went through it

arr2 = []

def addto(i,i2,i3,i4):
    arr2.append(i)
    arr2.append(i2)
    arr2.append(i3)
    arr2.append(i4)
    arr2.sort()
    print 'The min number in the array is ', arr2[0] , 'and the max is ', arr2[3]

addto(34,18,2,12)
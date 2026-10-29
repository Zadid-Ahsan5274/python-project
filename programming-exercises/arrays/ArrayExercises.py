from array import *
array_num = array('i',[1,3,5,7,9])

for i in array_num:
    print(i)

print("Accessing first 3 elements individually...")
print(f"{array_num[0]}  {array_num[1]}  {array_num[2]}")

print("Appending 11 at the end of the array...")
array_num.append(11)
print("New array: ", array_num)
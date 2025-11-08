import array as arr

#create an array
array_num=arr.array("i",[1,3,5,3,7,9,3])
print("original array", array_num)

print("Number of occurences of the nuber 3 in the said array",array_num.count(3))

#reverse the array
array_num.reverse()
print("reverse the order of an array", array_num)
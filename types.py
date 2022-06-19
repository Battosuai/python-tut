print("The loser says hello")
data1 = 10
data2 = 0x68
print(data1 + data2)
print(data2)

myStr = "Hello World"

print(myStr[0:3])

list1 = [9, 23, "keno"]
list2 = ["Living", "Hell"]

print(list1[0:2])
print(list1 + list2)

#Tuples cannot be edited where lists can
tuple1 = ('abcd', 786, 2.23, 'john', 70.2)
tuple2 = (123, 'john')

print(tuple1[0:2])
print(tuple1 + tuple2)

dict1 = {}
dict1['one'] = "This is one"
dict1[2] = "This is two"
dict2 = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict1['one'])
print(dict1[2])
print(dict2)
print(dict2.keys())
print(dict2.values())

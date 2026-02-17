fruits=["apple", "banana", "cherry","mango"]
vegetables=["carrot", "tomato", "spinach","cabbage"]
beverages=["water", "juice", "soda","tea"]

fruits.append("orange")
vegetables.insert(1,'brinjal')
beverages.pop()

inventory=[fruits,vegetables+beverages]
print(inventory)

print(list1)
print(fruits[0:2])
print(vegetables[-1])

if "water" in beverages:
    print("Water is available in beverages.")
    
l=[] 
for fruit in fruits:
    l.append(len(fruit))
print(l)
    
    
tuple1=(fruits[0],vegetables[0],beverages[0])
print(tuple1)
    
    
    
    









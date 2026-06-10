item1=input('Enter the new item:')
import os
if not os.path.exists("items.txt"):
    f=open("items.txt","w")
    f.write(item1+"\n")
    f.close()
else:
    f=open("items.txt","a")
    f.write(item1+"\n")
    f.close()
f=open("items.txt","r")
content=f.read()
print(content)




import os
if os.path.exists('students.txt'):
    f=open("students.txt","r")
    print("\nThe existing students are:\n")
    print(f.read())
    f.close()
    
n=int(input('How many students you want to add?'))
f=open("students.txt","a")
i=1
while i<=n:
    name=input('Enter the name:')
    f.write(name+"\n")
    i+=1
f.close() 
f=open("students.txt","r")
print("\nThe list of students:\n")
print(f.read())
f.close()

  

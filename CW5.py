python={"Reshma","Akshay","Riya","Shivani","Sam"}
data_science={"Rohit","Anjali","Sam","Riya"}
python.add("Sana")
data_science.remove("Sam")


print('Students enrolled in both courses:',python.intersection(data_science))
print('Students enrolled in only Python:',python.difference(data_science))
print('Students enrolled in either course:',python.union(data_science))

course_count={"Python":len(python),"Data Science":len(data_science)}
print(course_count)

for course, count in course_count.items():
    print(f"course:{course}, count:{count}")
    
growth = {course: count * 2 for course, count in course_count.items()}
print("Expected growth:", growth)










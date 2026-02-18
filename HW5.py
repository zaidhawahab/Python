frontend = {"Aisha", "Rahul", "Neha", "Arjun", "Sara"}
backend = {"Rahul", "Vikram", "Neha", "Priya", "Kiran"}

backend.add("Ankit")

frontend.remove("Sara")

print("Students enrolled in both courses:", frontend.intersection(backend))

print("Students enrolled only in Backend:", backend.difference(frontend))

unique_students = frontend.union(backend)
print("Total number of unique students:", len(unique_students))

course_counts = {
    "Frontend": len(frontend),
    "Backend": len(backend)
}

for course, count in course_counts.items():
    print(course, ":", count)

new_course_counts = {course: count for course, count in course_counts.items()}
new_course_counts["Fullstack"] = course_counts["Frontend"] + course_counts["Backend"]

print("Updated course dictionary:", new_course_counts)

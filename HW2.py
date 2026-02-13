course='''Learn Python from scratch and build real-world applications with ease.
This python course covers core concepts and advanced topics like web development and AI, helping you code with confidence.''' 


print('Length of the course description is:',len(course),'characters')

print('First character=',course[0])
print('Last character=',course[len(course)-1])

print('PREVIEW:',course[0:50])

new=course.replace('Python','PYTHON')
print(new)

new_lower=new.lower()
print(new_lower)

edited=new_lower.strip()
print(edited)

words=edited.split()
print('List of words in this paragraph=', words)

check='course' in course
print(check)

if check==True:
    print('The word "course" is present in the course description.')

final_msg="The course description is {} characters long and has {} words."
no_of_characters=len(edited)
no_of_words=len(words)

print(final_msg.format(no_of_characters,no_of_words))
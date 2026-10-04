# list of students named Jon, Kim, and Lee
students = ['Jon', 'Kim', 'Lee']
students.append('Sara')
students.append('Miko')

# change Jon to John
students[0] = 'John'

# function to print 'Hi name' for each student in the list and total number of students
def print_greetings():
    print(f"Total students: {len(students)}")
    for student in students:
        print(f"Hi {student}")

# call the function
print_greetings()
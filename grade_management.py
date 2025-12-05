"""
add
update
delete
veiw
exit



student =  {
    'vivek' : 100,
    'anuj' : 200
}
#accessing the value
print(student['anuj'])

#update the vale
student['anuj'] = 300

print(student['anuj'])

del(student['vivek'])
print(student)

"""
student_grade = {  }

def add_student(name , grade ):
    student_grade[name]= grade

    print(f'{name} is added to your list')

def update_student(name , grade ):
    if name in student_grade :
        student_grade[name]= grade
        print(f'{name} is updated with {grade}')
    else:
        print(f'{name} is not in {student_grade}')   #NAME IS NOT FOUND     

def delete_student(name):
    if name in student_grade :
        del (student_grade[name])
        print(f'{name} has been successfully deleted')
    else:
        print(f'{name}is not found')
#VIEW ALL STUDENT IN THE LIST   
def display_all_student (  ):
         # print (student_grade)
 
    if student_grade :
        for name , grade in student_grade.items():
            print(f'{name}, {grade} Here are the list of all the student in the list')

    else:
        print("The list is empty , if you want to add some student name so you can add here in the list of the student")



def main ():

    while True:
        print("\n The list of student with there grade")
       
        print("1. Add the name of the student ")
        print("2. update the name of the student you want to upadate")
        print("3. delete the name of the student ")
        print("4. veiw the name of the student in the list")
        print("5. Exit")

        choice = input("enter your choice ")
        if choice == '1' :
            name = input("enter the name of the student you want to add : = ")
            grade = input("enter the grade of the student you added : = ")
            add_student(name,grade)
        

        elif  choice == '2' :
            name = input("enter the name of the student you want to update")
            grade = input("enter the grade of the student you want to update")
            update_student(name , grade)

        elif choice == '3':
            name = input("enter the student name you want to delete")
            delete_student(name)

        elif choice == '4' :
            display_all_student( )

        elif choice == '5' :
            print("_________________")

            break
        else:
            print("invalid choice")

main()
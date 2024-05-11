'''
Problem (Intermediate - OOP):
Create a class called Student with attributes name, age, and grade. 
Include methods to display student information and update the grade.
Include methods to calculate the average grade of a list of students and to find the oldest student.
'''

class Student():

    def __init__(self, name, age, grade):
        self.name= name
        self.age= age
        self.grade= grade

    def student_info(self):
        return {"Name: ": self.name, "Age: ": self.age, "Grade: ": self.grade}
    
    def update_grade(self, new_grade):
        self.grade= new_grade
        return self.grade
    
    def average_grade(list):
        total=0
        for item in list:
            total += item.student_info()["Grade: "]
        return total/len(list)
    def old(list):
        age_list=[item.student_info()["Age: "] for item in list]
        return list[age_list.index(max(age_list))].student_info()["Name: "]
         
    

alice= Student("Alice", 14, 9)
bob = Student("Bob", 10, 5)
charlie = Student("Charlie", 17, 12)

#print("Alice information :", alice.student_info())
alice.update_grade(10)
print("Alice information :", alice.student_info())
print("Bob information :", bob.student_info())
print("Charlie information :", charlie.student_info())


print("Average grade: ", Student.average_grade([alice,bob, charlie]))
print("Oldest: ", Student.old([alice,bob, charlie]))

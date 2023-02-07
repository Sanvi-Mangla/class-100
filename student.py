class Student(object):
    def __init__(self,name,level,gender,age,grades=None):
        self.name=name
        self.level=level
        self.gender=gender
        self.age=age
        self.grades=grades or {}

    # function to set the grades of different courses/subjects
    def set_grades(self, course, grade):
        self.grades[course]=grade

    #function to get the grades
    def get_grades(self, course):
        return self.grades[course]

    def get_gpa(self):
        return sum ((self.grades.values())/len(self.grades))

#define some students
sanvi= Student("Sanvi","8th","female",14,{"maths":9})
khushi=Student("Khushi","8th","female",13,{"maths":7})

print(sanvi.name)
print(khushi)

        

        



#This is the StudentID class

class StudentID:
    def __init__(self, n, f, l, d, g):
        self.number = n
        self.first_name = f
        self.last_name = l
        self.date_of_birth = d
        self.grade_level = g
        
    def change_number(self, n):
        self.number = n
        
    def change_first_name(self, f):
        self.first_name = f
        
    def change_last_name(self, l):
        self.last_name = l
        
    def change_date_of_birth(self, d):
        self.date_of_birth = d
        
    def update_grade_level(self):
        self.grade_level = self.grade_level + 1
        
StudentID1 = StudentID("2026-45210", "Juan", "Dela Cruz", "10/23/07", 8)
StudentID2 = StudentID("3125-12141", "Pedro", "Garcia", "02/14/05", 5)

print("Number before:", StudentID1.number)
StudentID1.change_number("3125-12141")
print("Number after:", StudentID1.number)

print("First_name before:", StudentID1.first_name)
StudentID1.change_first_name("Pedro")
print("First_name after:", StudentID1.first_name)

print("Last_name before:", StudentID1.last_name)
StudentID1.change_last_name("Garcia")
print("Last_name after:", StudentID1.last_name)

print("Date_of_birth before:", StudentID1.date_of_birth)
StudentID1.change_date_of_birth("02/14/05")
print("Date_of_birth after:", StudentID1.date_of_birth)

print("Before update_grade_level:", StudentID1.grade_level)
StudentID1.update_grade_level()
print("After update_grade_level:", StudentID1.grade_level)


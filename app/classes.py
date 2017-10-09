students = []


class Student:

	school_name = "Morty Town Elementary"

	def __init__(self, name, last_name="Junior", student_id=9696):
		self.name = name
		self.last_name = last_name
		self.student_id = student_id
		students.append(self)

	def __str__(self):
		return "Student " + self.name + self.last_name

	def get_name_capitalize(self):
		return self.name.capitalize()

	def get_last_name_capitalize(self):
    		return self.last_name.capitalize()

	def get_school_name(self):
		return self.school_name


class HighSchoolStudent(Student):

	school_name = "Morty High School"

	def get_school_name(self):
		return "This is a High School student"

	def get_name_capitalize(self):
		original_value = super().get_name_capitalize()
		return original_value + "-HS"

rick = HighSchoolStudent("rick")
print(rick.get_name_capitalize())
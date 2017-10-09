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

	def get_last_name_capatilize(self):
    		return self.last_name.capitalize

	def get_school_name(self):
		return self.school_name
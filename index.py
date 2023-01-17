import json

class gender:
	FEMALE = "female"
	MALE = "male"
	BOTH = "both"
	def __init__(self, filename = "dataset.json"):
		read = open(filename, "r")
		self.file = json.loads(read.read())
		self.name = filename

	def getGender(self, name):
		name = name.lower()
		gender = 2
		if name in self.file['male'] and name in self.file['female']:
			gender = 2
		elif name in self.file['male']:
			gender = 1
		elif name in self.file['female']:
			gender = 0
		
		return gender
	
	def setGender(self, name, gender="both"):
		name = name.lower()
		gender = gender.lower()
		if gender == self.FEMALE or gender == self.BOTH:
			self.file[self.FEMALE] += name + ", "
		if gender == self.MALE or gender == self.BOTH:
			self.file[self.MALE] += name + ", "
		file = open(self.name, "w")
		file.write(json.dumps(self.file))

gender = gender()
print("Set names:")
while True:
	name = input("Please enter a name: ")
	if name == "":
		break
	gen = input("Enter either male, female, or both: ")
	gender.setGender(name, gen)


name = input("Enter a name to check: ")
print(gender.getGender(name))
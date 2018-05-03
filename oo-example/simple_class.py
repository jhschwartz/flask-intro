class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def get_species(self):
		return self.species

	def get_name(self):
		return self.name

	def print_species(self):
		print(self.species)

	@staticmethod
	def static_extract_info(animal):
		return animal.get_name() + " is of the species " + animal.get_species()

def run():
	jake = Animal(name='Jacob Schwartz', species="homo sapien")
	jake.print_species()
	print(Animal.static_extract_info(jake))

if __name__ == '__main__':
	run()
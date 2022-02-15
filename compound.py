PREFIXES = {1:"mono", 2:"di", 3:"tri", 4:"tetra", 5:"penta", 6:"hexa", 7:"hepta", 8:"octo", 9:"nona", 10:"deca"}

class compound:
	formula = {}
	charge = 0
	name = ""

	def compound(self, _formula, _charge = 0):
		self.formula = _formula
		self.charge = _charge
		name = calculate_name(_formula)
	
	def calculate_name(self, formula):
		compound_name = ""
		for element in formula.keys():
			# add the element's name to the name with its prefix
			compound_name += PREFIXES[formula[element]] + " "
		return compound_name

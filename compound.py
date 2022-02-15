class compound:
	formula = {}
	charge = 0
	name = ""

	def compound(self, _formula, _charge = 0):
		self.formula = _formula
		self.charge = _charge
		name = calculate_name(_formula)
	
	def calculate_name(self, formula):
		return "COMPOUND_NAME"

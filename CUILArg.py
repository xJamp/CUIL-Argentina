class CUIL():
	def __init__(self, Dni, Sexo):
		self.dni = Dni.replace('.', '')
		self.sexo = Sexo
		self.get = ''
		self.get_dni()
		self.get_sexo()
		self.get_cuil()

	def get_dni(self):
		if len(self.dni) == 7:
			self.dni = '0' + self.dni
			return True
		elif len(self.dni) != 8:
			return False

	def get_sexo(self):
		if self.sexo.startswith('f'):
			self.sexo = 'f'
		elif self.sexo.startswith('m'):
			self.sexo = 'm'
		else:
			return False
		return True

	def get_cuil(self):
		self.get = ''

		if self.sexo == 'f':
			self.get += '27'
		else:
			self.get += '20'
		self.get += '-'
		self.get += self.dni

		Suma_digitos = str(11 - (int(self.get[0])*5 + int(self.get[1])*4+ int(self.get[3])*3+ int(self.get[4])*2+ int(self.get[5])*7+ int(self.get[6])*6+ int(self.get[7])*5+ int(self.get[8])*4+ int(self.get[9])*3+ int(self.get[10])*2) % 11)

		if Suma_digitos == '11':
			Suma_digitos = '0'
		elif Suma_digitos == '10':
			Suma_digitos = '9'

		self.get += '-'
		self.get += Suma_digitos

def get(Dni, Sexo):
	return CUIL(Dni = Dni, Sexo = Sexo).get
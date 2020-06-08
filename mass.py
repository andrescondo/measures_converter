def value():
	value = float(input('Ingrese el valor a convertir: '))
	return value

class Mass:
	def kgAG(self):
		print('Convertir de kg a G')
		kg = value()
		g = kg * 1000
		print(' {} Kilogramos, equivale a {:.3f} Gramos'.format(kg,g))

	def GaKg(self):
		print('Convertir de Gramo a kg')
		g = value()
		kg = g / 1000
		print(' {} Gramo, equivale a {:.3f} Kilogramos'.format(g,kg))

	def KgaLb(self):
		print('Convertir de Kilogramos a libras')
		kg = value()
		lb = kg / 2.2                   #reducir el n# de decimales
		print(' {} Kilogramos, equivale a {:.3f} libras'.format(kg, lb))

	def LbaKg(self):
		print('Convertir de Libras a Kilogramos')
		lb = value()
		kg = lb * 0.453
		print(' {} Libras, equivale a {:.3f} Kilogramos'.format(lb, kg))

	def GaOnz(self):
		print('Convertir de Gramos a Onzas')
		g = value()
		onz = g * 0.035
		print(' {} Gramos, equivale a {:.3f} Onzas'.format(g, onz))

	def OnaAG(self):
		print('Convertir de Onzas a Gramos')
		onz = value()
		g = onz * 28.3495
		print(' {} Onzas, equivale a {:.3f} Gramos'.format(onz. g))


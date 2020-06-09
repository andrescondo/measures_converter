def value():
	value = float(input('Ingrese el valor a convertir: '))
	return value
M = ('Gramos', 'Kilogramos', 'Libras', 'Onzas')

class Mass:
	def kgAG(self):
		print('Convertir de {} a {}'.format(M[1], M[0]))
		kg = value()
		g = kg * 1000
		print(' {} {}, equivale a {:.3f} {}'.format(kg, M[1],g,M[0]))

	def GaKg(self):
		print('Convertir de {} a {}'.format(M[0],M[1]))
		g = value()
		kg = g / 1000
		print(' {} {}, equivale a {:.3f} {}'.format(g,M[0],kg,M[1]))

	def KgaLb(self):
		print('Convertir de {} a {}'.format(M[1],M[2]))
		kg = value()
		lb = kg / 2.2                   #reducir el n# de decimales
		print(' {} {}, equivale a {:.3f} {}'.format(kg,M[1], lb,M[2]))

	def LbaKg(self):
		print('Convertir de {} a {}',format(M[2],M[1]))
		lb = value()
		kg = lb * 0.453
		print(' {} {}, equivale a {:.3f} {}'.format(lb,M[2] ,kg,M[1]))

	def GaOnz(self):
		print('Convertir de {} a {}'.format(M[1],M[3]))
		g = value()
		onz = g * 0.035
		print(' {} {}, equivale a {:.3f} {}'.format(g,M[1], onz,M[3]))

	def OnaAG(self):
		print('Convertir de {} a {}'.format(M[3],M[0]))
		onz = value()
		g = onz * 28.3495
		print(' {} {}, equivale a {:.3f} {}'.format(onz,M[3], g,M[0]))


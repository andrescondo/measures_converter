
def value():
	value = float(input('Ingrese el valor a convertir: '))
	return value
M = ('Centimetros','Metros','Kilometros', 'Pies', 'Pulgadas', 'Millas')

class Length:
	
	def mAKm(self):
		print('Convertir de {} a {}'.format(M[1],M[2]))
		m = value()
		km = m / 1000
		print(' {} equivale a, {} {}'.format(m, km, M[2]))

	def mACm(self):
		print('Convertir de {} a {}'.format(M[1],M[0]))
		m = value()
		cm = m * 100
		print('{} equivale a {} {}'.format(m, cm, M[0]))

	def cmAM(self):
		print('Convertir de {} a {}'.format(M[0],M[1]))
		cm = value()
		m = cm 
		print('{} equivale a {} {}'.format(cm, m, M[0]))


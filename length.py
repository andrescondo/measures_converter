
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

	def KmAM(self):
		print('Convertir de {} a {}'.format(M[2], M[1]))
		cm = value()
		km = cm * 1000
		print(' {} {} equivale a {} {}'.format(cm,M[2],km, M[1]))

	def mAFt(self):
		print('Convertir de {} a {}'.format(M[1], M[3]))
		m = value()
		ft = m / 0.304
		print(' {} {} equivale a {} {}'.format(m,M[1],ft,M[3]))

	def cmAIn(self):
		print('Convertir de {} a {}'.format(M[0], M[4]))
		cm = value()
		In = cm * 0.393
		print(' {} {} equivale a {} {}'.format(cm,M[0],In, M[4]))

	def miAKm(self):
		print('Convertir de {} a {}'.format(M[5], M[2]))
		mi = value()
		km = mi * 1.609
		print('{} {}  equivale a {} {}'.format(mi,M[5],km, M[2]))



def value():
	value = float(input('Ingrese el valor a convertir: '))
	return value

class Length:
	def mAKm(self):
		print('Convertir de metros a Kilometros')
		m = value()
		km = m * 1000
		print(' {} equivale a, {} Kilometros'.format(m, kg))

	def mACm(self):
		print('Convertir de Metros a centimetros')
		m = value()
		cm = m / 100
		print('{} equivale a {} centimetros'.format(m, cm))

	def cmAM(self):
		print('Convertir de centimetros a Metros')
		cm = value()
		m = cm 
		print('{} equivale a {} centimetros'.format(cm, m))


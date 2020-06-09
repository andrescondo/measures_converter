def value():
	value = float(input('Ingrese el valor a convertir: '))
	return value
	
L = ('Centimetros Cúbicos', 'Litros')
class Volume:
	def cmAL(self):
		print('Convertir de {} a {}'.format(L[0],L[1]))
		cm = value()
		lt = cm * 0.001
		print(' {} equivale, a {:.3f} {}'.format(cm, lt, L[1])) 

	def LAcm(self):
		print('Convertir de {} a {}'.format(L[1],L[0]))
		lt = value()
		cm = lt * 1000
		print(' {} equivale, a {:.3f} {}'.format(lt, cm,L[0]))


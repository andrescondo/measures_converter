def value():
	value = float(input('Ingrese el valor a convertir: '))
	return value

class Volume:
	def cmAL(self):
		print('Convertir de centimetros cúbicos a Litros')
		cm = value()
		lt = cm * 0.001
		print(' {} equivale, a {:.3f} Litros'.format(cm, lt)) 

	def LAcm(self):
		print('Convertir de Litros a centimetros cúbicos')
		lt = value()
		cm = lt * 1000
		print(' {} equivale, a {:.3f} centimetros cúbicos'.format(lt, cm))


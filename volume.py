def value():
	while True:
		value = input('Ingrese el valor a convertir: ')
		try:
			value = float(value)
			return value
		except ValueError:
			print('Ingrese números')
	
L = ('Centimetros Cúbicos', 'Litros', 'Milimetros cúbicos')
class Volume:
	def cmAL(self):
		print('Convertir de {} a {}'.format(L[0],L[1]))
		cc = value()
		lt = cc * 0.001
		print(' {} equivale, a {:.3f} {}'.format(cc, lt, L[1])) 

	def LAcm(self):
		print('Convertir de {} a {}'.format(L[1],L[0]))
		lt = value()
		cm = lt * 1000
		print(' {} equivale, a {:.3f} {}'.format(lt, cm,L[0]))

	def mcAL(self):
		print('Convertir de {} a {}'.format(L[2], L[1]) )
		mc = value()
		l = mc * 0.001
		print('{} {} equivale, a {} {}'.format(mc,L[2],l,L[1] ))

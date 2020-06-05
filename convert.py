# -*- coding: utf-8 -*-

def value():
	value = float(input('Ingrese el valor a convertir: '))
	return value

def kgAG():
	print('Convertir de kg a G')
	kg = value()
	g = kg * 1000
	print(' {} Kilogramos, equivale a {:.3f} Gramos'.format(kg,g))

def GaKg():
	print('Convertir de Gramo a kg')
	g = value()
	kg = g / 1000
	print(' {} Gramo, equivale a {:.3f} Kilogramos'.format(g,kg))

def KgaLb():
	print('Convertir de Kilogramos a libras')
	kg = value()
	lb = kg / 2.2                   #reducir el n# de decimales
	print(' {} Kilogramos, equivale a {:.3f} libras'.format(kg, lb))

def LbaKg():
	print('Convertir de Libras a Kilogramos')
	lb = value()
	kg = lb * 0.453
	print(' {} Libras, equivale a {:.3f} Kilogramos'.format(lb, kg))

def GaOnz():
	print('Convertir de Gramos a Onzas')
	g = value()
	onz = g * 0.035
	print(' {} Gramos, equivale a {:.3f} Onzas'.format(g, onz))

def OnaAG():
	print('Convertir de Onzas a Gramos')
	onz = value()
	g = onz * 28.3495
	print(' {} Onzas, equivale a {:.3f} Gramos'.format(onz. g))



def mass_convert():
	while True:
		mass = str(input('''
		===================================
			C O N V E R T I D O R 
			Ingrese la medida a convertir
			[1] Kg a G
			[2] G a Kg
			[3] Kg a Lb
			[4] Lb a Kg
			[5] G a Onz
			[6] Onz a G

			[s]alir
			''')).lower()

		if mass == '1':
			kgAG()
		elif mass == '2':
			GaKg()
		elif mass == '3':
			KgaLb()
		elif mass == '4':
			LbaKg()
		elif mass == '5':
			GaOnz()
		elif mass == '6':
			OnaAG()

		elif mass == 's':
			break
		else:
			print('Ingreso un dato invalido')

def cmAL():
	print('Convertir de centimetros cúbicos a Litros')
	cm = value()
	lt = cm * 0.001
	print(' {} equivale, a {:.3f} Litros'.format(cm, lt)) 

def LAcm():
	print('Convertir de Litros a centimetros cúbicos')
	lt = value()
	cm = lt * 1000
	print(' {} equivale, a {:.3f} centimetros cúbicos'.format(lt, cm))



def volume_convert():
	while True:
		volume = str(input('''
		===================================
			C O N V E R T I D O R 
			Ingrese la medida a convertir

			[1] centimetro cúbico a Litro
			[2] de Litros a centimetro cúbico

			[s]alir
			''')).lower()

		if volume == '1':
			cmAL()

		elif volume == '2':
			LAcm()

		elif volume == 's':
			break
		else:
			print('Ingreso un dato invalido')




def run():
	while True:
		option = str(input('''
		==================================
			Escoga el tipo de conversión
			[m]asa
			[v]olumen

			[s]alir
			''')).lower()

		if option == 'm':
			mass_convert()
		elif option == 'v':
			volume_convert()


		elif option == 's':
			break
		else:
			print('Ingreso un dato invalido')


if __name__ == '__main__':
	run()

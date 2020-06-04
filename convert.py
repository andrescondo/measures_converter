# -*- coding: utf-8 -*-

def kgAG():
	print('Convertir de kg a G')
	kg = float(input('Ingrese el valor a convertir: '))
	g = kg * 1000
	print(' {} Kilogramos, equivale a {} Gramos'.format(kg,g))

def GaKg():
	print('Convertir de Gramo a kg')
	g = float(input('Ingrese el valor a convertir: '))
	kg = g / 1000
	print(' {} Gramo, equivale a {} Kilogramos'.format(g,kg))





def run():

	while True:
		option = str(input('''
		===================================
			C O N V E R T I D O R 
			Ingrese la medida a convertir
			[1] Kg a G
			[2] G a Kg

			[s]alir
			''')).lower()

		if option == '1':
			kgAG()

		elif option == '2':
			GaKg()

		elif option == 's':
			break



if __name__ == '__main__':
	run()

# -*- coding: utf-8 -*-
from mass import Mass
from volume import Volume
from length import Length

def title():
	title = print('''
		Ingrese la medida a convertir 
		----------------------------------''')
	

def mass_convert():
	mass = Mass()

	while True:
		title()
		option = str(input('''
			[1] Kg a G
			[2] G a Kg
			[3] Kg a Lb
			[4] Lb a Kg
			[5] G a Onz
			[6] Onz a G

			[s]alir
			''')).lower()

		if option == '1':
			mass.kgAG()
		elif option == '2':
			mass.GaKg()
		elif option == '3':
			mass.KgaLb()
		elif option == '4':
			mass.LbaKg()
		elif option == '5':
			mass.GaOnz()
		elif option == '6':
			mass.OnaAG()

		elif option == 's':
			break
		else:
			print('Ingreso un dato invalido')



def volume_convert():
	volume = Volume()
	while True:
		title()
		option = str(input('''
			[1] centimetro cúbico a Litro
			[2] de Litros a centimetro cúbico

			[s]alir
			''')).lower()

		if option == '1':
			volume.cmAL()

		elif option == '2':
			volume.LAcm()

		elif option == 's':
			break
		else:
			print('Ingreso un dato invalido')



def length_convert():
	length = Length()
	while  True:
		title()
		option = str(input('''
			[1] m a Km
			[2] m a cm
			[3] cm a m
			[4] Km a m
			[5] m a ft
			[6] cm a in
			[7] mi a Km

			[s]alir

			''')).lower()

		if option == '1':
			length.mAKm()
		elif option == '2':
			length.mACm()
		elif option == '3':
			length.cmAM()
		elif option == '4':
			length.kmAM()
		elif option == '5':
			length.mAFt()
		elif option == '6':
			length.cmAIn()
		elif option == '7':
			length.miAKm()
		elif option == 's':
			break

		else:
			print('Ingreso de dato no valido')


def run():
	while True:
		option = str(input('''
		==================================
			C O N V E R T I D O R 
		==================================
			Escoga el tipo de conversión
			[m]asa
			[v]olumen
			[l]ongitud

			[s]alir
			''')).lower()

		if option == 'm':
			mass_convert()
		elif option == 'v':
			volume_convert()
		elif option == 'l':
			length_convert()
		elif option == 's':
			break
		else:
			print('Ingreso un dato invalido')


if __name__ == '__main__':
	run()


# Convertidor de medidas
## Convierte medidas de : 
- longitud
- volumen
- masa

## Requerimientos:
> El Programa usa Python 3, Asegurarse de tener esta versión para su correcto funcionamiento
[Descarga Python](https://www.python.org/downloads/)
 
## Funcionamiento
El programa Funciona con un menú donde se podrá escoger entre los tres tipos de conversiones.

En el menu principal, cuenta con un ciclo para el ingreso de las opciones, en caso de escoger una que no sean las especificadas, se repetirá la petición para el ingreso, incluyendo que cuenta con una opcíón para salir del programa.

Dentro de cada uno de estos menús se tiene acceso a diferentes formas de conversión. Estos valores podrán ser ingresados tanto en números enteros o decimales. Los datos ingresados en caso de ser decimales, se deberá de separar con puntos y no con comas, en caso de ser ingresados con comas esto mandara error y pedirá que ingrese el dato nuevamente.
Así mismo, si los datos ingresados son letras, o caracteres alfanúmericos, esto arrojará el mensaje de error, y pedirá nuevamente el reingreso.

El programa emplea uso de módulos para cada uno de los tipos de conversión, siendo así más legible para el desarrollador.
Los módulos están separados por el tipo de conversión que se realizarán, esta es invocada en cada una de las opciones de conversión.

Cada módulo hace uso de tuplas, ayudando asi a aligerar el peso del programa, por la reduccion de palabras repetidas, y facilitando a futuros ingresos de mas medidas de conversión. Además de usar una función recursiva para el ingreso de las medidas a convertir, siendo esta función la encargada de validar los valores para evitar el ingreso de caracteres erróneos y el cierro del programa por estos errores.


## Lista de tareas
- [x] Uso de módulos
- [x] Reducir el texto, usando tuplas
- [x] Validación para errores

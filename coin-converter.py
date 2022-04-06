#solicitamos el monto de dinero a convertir
pesos = input('¿Cuantos pesos tienes?: ')
#transformamos el numero que nos da, en un numero flotante
pesos = float(pesos)
#definimos el valor de la moneda a convertir
valor_dolar = 200
#realizamos el calculo de conversion
dolares = pesos / valor_dolar
#con round le decimos cuantos decimales queremos que tenga
dolares = round(dolares, 2)
#lo transformamos en texto para poder mostrarlo
dolares = str(dolares)
#lo mostramos con print y concatenando texto y numero
print('Tienes $' + dolares + ' Dolares')

#reto: convertir el ejemplo en un programa de conversión

menu = """
Bienvenido al conversor de monedas ($)

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: 
"""

opcion = int(input(menu))

if opcion == 1:
    pesos = float(input('¿Cuantos pesos colombianos tienes?: '))
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares)
elif opcion == 2:
    pesos = float(input('¿Cuantos pesos arentinos tienes?: '))
    valor_dolar = 200
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares)
elif opcion == 3:
    pesos = float(input('¿Cuantos pesos mexicanos tienes?: '))
    valor_dolar = 38
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares)
else:
    print('Ops! Intente nuevamente')
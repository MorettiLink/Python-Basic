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


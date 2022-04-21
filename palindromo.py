def palindromo(palabra):
    palabra = palabra.strip()
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

def palindromo2(string):
    try:
        if len(string) == 0:
            raise ValueError('No se puede ingresar una cadena vacia')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

def palindromo3(string):
    assert len(string) > 0, 'No se puede ingresar una cadena vacia'
    return string == string[::-1]

try:
    print(palindromo2(" "))
except TypeError:
    print('solo se pueden ingresar strings')

def run():
    palabra = str(input('Escribe una palabra o frase: '))
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo!')
    else:
        print('No es Palindromo :(')


if __name__ == '__main__':
# Este código se lama 'entry point' 
# Cuando python se encuentra con ese código, comienza a correr todo lo que esta debajo
    run()


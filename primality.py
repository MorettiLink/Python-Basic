# Buscando numeros primos
def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        elif numero % i == 0:
            contador += 1
    
    if contador == 0:
        return True
    else:
        return False


def primal(number):
    fact = 1
    for i in range(1, number):
        fact = fact * i
    if (fact + 1) % number == 0:
        return 'Its primal'
    else:
        return 'Its not primal'


def run():
    numero = int(input('Escribe un número: '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')

    number = int(input('Insert a number to search: '))
    answer = primal(number)
    print(answer)

# funciones anonimas
    palindromo2 = lambda string: string == string[::-1]
# variable = argumento: expresion
# variable = <- retorna un objeto de tipo función
    print(palindromo2(str(input('ingrese otra palabra: '))))


if __name__ == '__main__':
    run()



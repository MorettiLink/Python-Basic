# Guess the number in range of 1 to 100 with help
import random

def run():
    print('Hi! try to guess the number beyond 1 to 100, good luck!')

    num_chosen = int(input('Which number can be? >>> '))
    num_random = random.randint(1, 100)
    cont = 1

    while num_chosen != num_random:
        if num_chosen > num_random:
            num_chosen = int(input('Too big! Try smaller >>> '))
            cont += 1
        else:
            num_chosen = int(input('Too small! Try bigger >>> '))
            cont += 1
    
    print('Correct! Well done :)')
    print('Attempts: ' + str(cont))


if __name__ == '__main__':
    run()
import random
import string

def generate_password():
    # MAYUS = ['A','B','C','D','E','F,','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    # MINUS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    # NUMS = [0,1,2,3,4,5,6,7,8,9]
    # SYMBOL = ['*','+','-','/','@','_','?','¿','!','[',']','{','}','(',')',',','.',';',':','<','>','~','°','|','¬','·','½,','"','#','$','%','&','=','==','===','´','^','`',' ']

    mayus = list(string.ascii_uppercase)
    minus = list(string.ascii_lowercase)
    simbol = list(string.punctuation)
    numbers = list(string.digits)
    space = list(string.whitespace)

    character_list = mayus + minus + simbol + numbers + space

    password = []

    password_width = int(input('¿Cúantos dígitos debe tener la contraseña? '))

    for i in range(password_width):
        character_random = random.choice(character_list)
        password.append(character_random)

    password = "".join(password)
    return password

def run():
    password = generate_password()
    print('Tu nueva contraseña es: ' + password)



if __name__ == '__main__':
    run()
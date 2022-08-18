#condiciones anidadas elif

sensorniveldeagua=int(input("Digite el nivel de agua actual"))

if(sensorniveldeagua >= 0 and sensorniveldeagua < 20):
    print(f'Peligro el nivel {sensorniveldeagua} es peligroso')
elif(sensorniveldeagua >=20 and sensorniveldeagua <400):
    print(f'El nivel del agua esta en un nivel adecuado {sensorniveldeagua}')
elif(sensorniveldeagua >=400):
     print(f'Peligro el nivel {sensorniveldeagua} es peligroso')    
else:
     print(f'El nivel del agua no es valido')
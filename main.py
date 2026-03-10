import random
def startGame():
number = random.randint(1, 20)
guess = 0
attempts = 0
print("Adivina el número entre 1 y 20")
while guess != number:
guess = int(input("Ingresa tu intento: "))
attempts += 1
if guess < number:
print("Muy bajo")
elif guess > number:
print("Muy alto")
elif guess == number:
print("¡Correcto!")
else:
print("Error")
print("Número de intentos:", attempts)
startGame()

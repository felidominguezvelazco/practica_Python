import random
words = categorias = {
    "programacion": ["python", "variable", "funcion", "bucle"],
    "animales": ["perro", "gato", "elefante", "tigre"],
    "frutas": ["manzana", "banana", "naranja", "pera"]
}
print("Categorías disponibles:")
for categoria in categorias:
    print(f"- {categoria}")
print()
eleccion = input("Elegí una categoría: ")
while eleccion not in categorias:
    print("Categoría no válida. Intenta de nuevo.")
    eleccion = input("Elegí una categoría: ")
words = categorias[eleccion]
word = random.choice(words)
guessed = []
attempts = 6
puntaje = 0
print("¡Bienvenido al Ahorcado!")
print()
while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        puntaje += 6
        print("¡Ganaste!")
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    letter = input("Ingresá una letra: ")
    if len(letter) != 1 or not letter.isalpha(): 
        print("Entrada no válida")
        print()
        continue
    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        puntaje -= 1
        print("Esa letra no está en la palabra.")
    print()
else:
    puntaje = 0
    print(f"¡Perdiste! La palabra era: {word}")
print(f"Tu puntaje final es: {puntaje}")
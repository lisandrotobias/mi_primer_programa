

chosen_pokemon = input("¿Contra qué Pokemon quieres combatir? (Squirtle / Charmander / Bulbasaur): ").upper()

pikachu_life = 100
enemy_life = 0
enemy_damage = 0


if chosen_pokemon == "SQUIRTLE":
    enemy_life = 90
    enemy_damage = 8
    name = "Squirtle"
elif chosen_pokemon == "CHARMANDER":
    enemy_life = 80
    enemy_damage = 7
    name = "Charmander"
elif chosen_pokemon == "BULBASAUR":
    enemy_life = 100
    enemy_damage = 10
    name = "Bulbasaur"


while pikachu_life > 0 and enemy_life > 0:
    chosen_attack = input("¿Qué ataque vamos a usar? (Placaje / Chispazo) ").upper()

    if chosen_attack == "CHISPAZO":
        enemy_life -= 12
        print("Le has hecho a {} de 12 de daño".format(name))
    elif chosen_attack == "PLACAJE":
        enemy_life -= 10
        print("Le has hecho a {} de 10 de daño".format(name))

    print("La vida de {} ahora es de {}".format(name, enemy_life))


    pikachu_life -= enemy_damage
    print("{} te hace un ataque de {} de daño".format(name, enemy_damage))

    print("La vida de Pikachu es de {}".format(pikachu_life))

if enemy_life <= 0:
    print("Has ganado")

elif pikachu_life <= 0:
    print("Has perdido")


print("El combate ha terminado")
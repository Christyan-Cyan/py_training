import random

my_health = 100
enemy_health = 100
print("Battle Was Begin !")

while my_health > 0 or enemy_health > 0:
    my_damage = random.randint(0, 30)
    enemy_damage = random.randint(0, 30)
    input_data = input("\nAttack ? ")
    if input_data == "yes":
        if my_damage == 30:
            print("Critical Damage ! \n")
        elif enemy_damage == 30:
            print("Enemy Critical ! \n")
        elif my_damage == 0 or enemy_damage == 0:
            print("no damage \n")
        enemy_health -= my_damage
        print("Your Damage :", my_damage)
        print("Enemy Turn")
        my_health -= enemy_damage
        print("Enemy Damage :", enemy_damage)
        print("My Health :", my_health, "\nEnemy Health :", enemy_health)
        if my_health <= 0:
            print("\nDefeat !")
            print("\nBattle Ends")
            print("Your Health :", my_health)
            print("Enemy Health :", enemy_health, "\n")
            break
        elif enemy_health <= 0:
            print("\nVictory !")
            print("\nBattle Ends")
            print("Your Health :", my_health)
            print("Enemy Health :", enemy_health, "\n")
            break
    elif input_data == "no":
        print("No Damage\nYour Health :", my_health)
        print("Enemy Health :", enemy_health, "\n")
        break
    else:
        print("???")

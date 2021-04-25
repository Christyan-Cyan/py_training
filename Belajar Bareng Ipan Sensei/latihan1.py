import random
# enemy_hp = 100

# while enemy_hp > 0:
#     inp_data = input("Attack ? ")
#     if inp_data == "yes":
#         enemy_hp -= 20
#         print("HP Enemy : ", enemy_hp)
#     elif inp_data == "no":
#         print("HP Enemy : ", enemy_hp)
#         break
#     else:
#         print("cuih")

# else:
#     print("Enemy Death")


# my_hp = 10

# while my_hp >= 10:
#     masuk_data = input("Heal ?")
#     if masuk_data == "yes":
#         my_hp += 10
#         print("My HP : ", my_hp)
#     elif masuk_data == "no":
#         print("My HP : ", my_hp)
#         break
#     else:
#         print("sssshhhh cring")

# else:
#     print("Yeeee")


my_health = 100
enemy_health = 100

while my_health >= 0 or enemy_health >= 0:
    my_damage = random.randint(0, 30)
    enemy_damage = random.randint(0, 30)
    input_data = input("Attack ? ")
    if input_data == "yes":
        enemy_health -= my_damage
        print("Your Damage :", my_damage)
        print("Enemy Turn")
        my_health -= enemy_damage
        print("Enemy Damage :", enemy_damage)
        print("My Health :", my_health, "\nEnemy Health :", enemy_health)
    elif input_data == "no":
        print("No Damage\nYour Health :", my_health)
        print("Enemy Health :", enemy_health)
        break
    else:
        print("???")

else:
    print("Battle Ends")
    print("Your Health :", my_health)
    print("Enemy Health :", enemy_health)

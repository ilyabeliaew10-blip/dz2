import time

inventory = []
has_key = False
has_sword = False


def print_pause(message, delay=2):
    print(message)
    time.sleep(delay)


def intro():
    print_pause("Вы стоите на перекрестке в древнем лесу.")
    print_pause("Вокруг вас три тропинки, ведущие в разные стороны.")
    print_pause("Северная тропа ведет к темному замку.")
    print_pause("Восточная тропа ведет к загадочной пещере.")
    print_pause("Западная тропа ведет к старому мосту.")


def make_choice(choices):
    while True:
        print("\nВыберите действие:")
        for i, choice in enumerate(choices, 1):
            print(f"{i}. {choice}")

        try:
            choice = int(input("Ваш выбор (введите номер): "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Пожалуйста, выберите номер из предложенных вариантов.")
        except ValueError:
            print("Пожалуйста, введите число.")


def castle_path():
    global has_key

    print_pause("\nВы подходите к мрачному замку.")

    if has_key:
        print_pause("У вас есть ключ! Вы открываете дверь и входите внутрь.")
        print_pause("В замке вы находите сокровищницу!")
        print_pause("ПОЗДРАВЛЯЮ! ВЫ НАШЛИ СОКРОВИЩЕ!")
        return "win"
    else:
        print_pause("Дверь замка заперта. Вам нужен ключ.")
        print_pause("Вы возвращаетесь на перекресток.")
        return "continue"


def cave_path():
    global has_key, has_sword

    print_pause("\nВы входите в темную пещеру.")

    choices = [
        "Осмотреть левую часть пещеры",
        "Осмотреть правую часть пещеры",
        "Вернуться на перекресток"
    ]

    while True:
        choice = make_choice(choices)

        if choice == 1:
            print_pause("В левой части пещеры вы находите старинный ключ!")
            has_key = True
            inventory.append("Ключ от замка")
            print("Инвентарь:", inventory)
        elif choice == 2:
            if has_sword:
                print_pause("Вы уже забрали меч отсюда.")
            else:
                print_pause("В правой части пещеры вы находите блестящий меч!")
                has_sword = True
                inventory.append("Стальной меч")
                print("Инвентарь:", inventory)
        else:
            print_pause("Вы возвращаетесь на перекресток.")
            return "continue"


def bridge_path():
    global has_sword

    print_pause("\nВы подходите к старому каменному мосту.")
    print_pause("Внезапно из-под моста появляется огромный тролль!")

    if has_sword:
        print_pause("Но у вас есть меч! Вы готовы к битве!")
        print_pause("После напряженного боя вы побеждаете тролля!")
        print_pause("За мостом вы находите деревню и в безопасности добираетесь до дома.")
        print_pause("ПОЗДРАВЛЯЮ! ВЫ ВЫИГРАЛИ!")
        return "win"
    else:
        print_pause("У вас нет оружия! Тролль атакует!")
        print_pause("К сожалению, вы не смогли защититься...")
        print_pause("ИГРА ОКОНЧЕНА")
        return "lose"


def game_loop():
    game_state = "playing"

    while game_state == "playing":
        intro()

        choices = [
            "Пойти на север (к замку)",
            "Пойти на восток (к пещере)",
            "Пойти на запад (к мосту)",
            "Посмотреть инвентарь",
            "Закончить игру"
        ]

        choice = make_choice(choices)

        if choice == 1:
            result = castle_path()
            if result in ["win", "lose"]:
                game_state = "ended"
        elif choice == 2:
            cave_path()
        elif choice == 3:
            result = bridge_path()
            if result in ["win", "lose"]:
                game_state = "ended"
        elif choice == 4:
            if inventory:
                print("\nВаш инвентарь:")
                for item in inventory:
                    print(f"- {item}")
            else:
                print("\nВаш инвентарь пуст.")
        else:
            print_pause("Спасибо за игру!")
            game_state = "ended"

    return input("\nХотите сыграть еще раз? (да/нет): ").lower().startswith('д')


def main():
    print("=== ТЕКСТОВАЯ ИГРА 'ПРИКЛЮЧЕНИЕ В ЛЕСУ' ===")
    print("Сделайте выбор, вводя цифру от 1 до 5")

    play_again = True
    while play_again:
        global inventory, has_key, has_sword
        inventory = []
        has_key = False
        has_sword = False

        play_again = game_loop()

    print("До свидания! Спасибо за игру!")


if __name__ == "__main__":
    main()
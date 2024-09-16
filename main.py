# nums = [7,8,9,3,1,2,]
#
# def bubble_sort(ls):
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(ls) - 1):
#             if ls[i]  > ls[i + 1]:
#                 ls[i], ls[i + 1] = ls[i + 1], ls[i]
#                 swapped = True
# #
# # bubble_sort(nums)
# # print(nums)
#
# def selection_sort(ls):
#     for i in range(len(ls)):
#         lowest = i
#         for j in range(i + 1, len(ls)):
#             if ls[j] < ls[lowest]:
#                 lowest = j
#         ls[i], ls[lowest] = ls[lowest], ls[i]
#
# selection_sort(nums)
# print(nums)
from math import floor


# hero_health = 100
# hero_inventory = []
#
# def find_item(item):
#     message = f'Вы нашли {item}'
#     hero_inventory.append(item)
#     print(message)
#
# def fight_monster(monster, damage):
#     global hero_health
#     hero_health -= damage
#     if hero_health > 0:
#         print(f'Вы сразилисиь с {monster} и получили {damage} урона. Осталось {hero_health} здоровья')
#     else:
#         print(f'Вы побеждены {monster}....')
#
# def show_status():
#     health_status = f'Здоровье героя: {hero_health}'
#     inventory_status = f'Инвентарь героя: {', '.join(hero_inventory) if hero_inventory else 'пусто'}'
#     print(health_status)
#
# #     print(inventory_status)
#
#
#
# def main():
#     find_item("меч")
#     find_item("щит")
#     show_status()
#     fight_monster('Гоблин', 30)
#     show_status()
#     fight_monster("Дракон", 80)
#     show_status()
#
#
# if __name__ == '__main__':
#     main()


# class Car:
#     def __init__(self, model, colour):
#         self.model = model
#         self.colour = colour
#
#     def start(self):
#         print(f'{self.model} {self.colour} на старте')
#
# my_car = Car('BMV', 'red')
# my_car.start()


# class House:
#     def __init__(self, floor, door):
#         self.floor = floor
#         self.door = door
#
#     def start(self):
#         print(f'Я нахожусь на {self.floor} этаже, квартира номер {self.door} ')
#
# my_house = House(5, 54)
# my_house.start()


class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_floors = floors

    def go_to(self,new_floor):
        if 1 <= new_floor <= self.number_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print(f'Такого этажа не существует')

    def __del__(self):
        print(f'{self.name} взорвался')




h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
del (h2)
h1.go_to(5)
# h2.go_to(10)




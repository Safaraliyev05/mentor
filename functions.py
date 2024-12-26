numbers = [1, 2, 3, 4, 5]
numbers2 = [4, 7, 12, 34]
numbers3 = [7, 80, 12, 5, 8]
from datetime import datetime

print(datetime.date)


def sonlar_yigindisi(sonlar):
    counter = 0

    for son in sonlar:
        counter += son
    print(counter)


# sonlar_yigindisi(numbers)
# sonlar_yigindisi(numbers2)
# sonlar_yigindisi(numbers3)

# n = input('ismini yoz: ')
# print(n)
# print(len(numbers2))
# print(max(numbers))
# print(min(numbers))

# def malumot(ism: str, familiya, yosh=18):
#     print(f'Meni ismim {ism}, familyam {familiya}, yoshim  {yosh}da')
#
#
# malumot('sardor', 'safaraliyev', 20)

def user_age():
    yil = input('Tugilgan yilingiz: ')
    oy = input('Tugilgan oyingiz: ')
    kun = input('Tugilgan kuningiz: ')


def func(*args, **kwargs):
    print(args)

func(1)
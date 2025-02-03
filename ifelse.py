# # def split_and_join(line):
# #     line = line.split()
# #     line = "-".join(line)
# #     return line
# #
# #
# # if __name__ == '__main__':
# #     line = input()
# #     result = split_and_join(line)
# #     print(result)
# #
# print("Salom mening ismim Anvar")
# print("Salom mening ismim Anvar ")
# print("Men PDP Juniorda Python kursida oqiyman")
# print(" Python dunyodagi eng yahshi dasturlash tilaridan biri")
# print(789 + 900)
# print(12 + 8)
# print(22 - 23)
# print(35 / 7)
# print(12 * 38)
# print(10 % 3)
# print(10 // 3)
# print(2 ** 3)
#
# print(15 % 5)
# print(8 ** 2)
#
# print(8 % 19)
# print(90 ** 89)
# print(77 + 84)


print("Assalamu alaykum Kalkulator dasturimizga xush keldingiz!")

number = int(input("1 chi sonni kiriting: "))
operator = input("""
                    + -> Qo'shish
                    - -> Ayirish
                    * -> Ko'paytirish
                    / -> Bo'lish
                    Quyidagi amallardan birini kiriting: """)
number2 = int(input("2 chi sonni kiriting: "))

if operator == "+":
    print(f"{number} + {number2} = {number+number2}")
elif operator == "-":
    print(f"{number} - {number2} = {number-number2}")
elif operator == "*":
    print(f"{number} * {number2} = {number*number2}")
elif operator == "/":
    if number != 0 and number2 != 0:
        print(f"{number} / {number2} = {number//number2}")
    else:
        print("0 ga bo'lish mumkin emas")
else:
    print("Noto'g'ri amal kiritildi !")

data_arr = []
salary_arr = []
amount = 0

for i in range(3):
    data_arr.append(input("Имя " + str(i + 1) + " человека"))

for i in range(3):
    salary_arr.append(input("Доход " + str(i + 1) + " человека"))


сredit = input("введите сумму кредита")
how_long = input("на какой срок кредит в месяцах")
procent = input("введите процент")

pay_per_month = (int(сredit) / int(how_long)) + ((int(сredit) / 100 * int(procent)) / 12)

print("Платеж за месяц", pay_per_month)

for salary in salary_arr:
    amount += int(salary)

amount -= pay_per_month
mean = amount / 3

mean = str(mean)
for name in data_arr:
    print(name + " может потратить " + mean)




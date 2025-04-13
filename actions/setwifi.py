import os

print("Если вы используете Network Manager, то это для вас")
print("Что вам нужно?")
print("1(лист wifi точек), 2(подключение к wifi)")

varw = input(": ")

if varw == "2":

	namewifi = input("Название wifi точки: ")
	passwifi = input("Пароль wifi точки: ")

	os.system('nmcli device wifi connect '+namewifi+' password '+passwifi)
	
	print('Готово!')


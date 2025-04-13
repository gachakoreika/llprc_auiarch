import os
import logging

##-------------------------
##        LOGGING
##-------------------------

#logstrime = logging.StreamHandler()
#logfile = logging.FileHandler("llprc/llprc_log.txt")

##-------------------------
##        PROGRAMM
##-------------------------

os.system('setfont cyr-sun16')

print("WElCOME! Это программа автоустановки системы Arch Linux(если вы выбрали только xorg и драйвер свой)")
print(" ")
print(" ")
print("Ver. 25.4-13")

print("Сделано gachak_")
print(" ")

print("Какое действие вы хотите сделать?")
print("Действия: 1(установить нужные пакеты), 2(настроить сеть через nmcli(Не написанно)), 3(установить wm/de)")
print("Для помощи введите h или help!")
print(" ")


var = input('Номер: ')

if var == "h" or var == "help":

    print("При просьбе ввести пароль sudo, вводите.")
    print("При просьбе ввести выборочное значение вводите")

    print(" ")

    print("Этот хелп меню необязательное к прочтению! Программа сама закроется, когда закончит всё! И она всё предупредит!")
    print("Лучше используйте archinstall в livecd arch linux, чем это самописанное изделие на python")

if var == "1":
    os.system('python llprc/actions/installs/in_apps.py')
    
if var == "2":

    os.system('python llprc/actions/setwifi.py')

if var == "3":
	
	os.system('python llprc/actions/installs/in_os.py')
	








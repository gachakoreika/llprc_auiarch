import os


print("ВЫ ХОТИТЕ ВЫБРАТЬ DE OR WM")
print("1(DE), 2(WM)")

var2 = input('ОТВЕТ: ')

print(" ")

if var2 == "1":

    print("1(XFCE), 2(KDE)")

    var3 = input('Ответ: ')

    if var3 == "1":

        print("ВНИМАНИЕ, СЕЙЧАС ПРОИСХОДИТ УСТАНОВКА XFCE, НЕ ТРОГАЙТЕ ОБОРУДОВАНИЕ!!!")

        os.system('sudo pacman -S xfce4 xfce4-goodies sddm')

        print("Внимание, у вас всё нужное установилось! У вас по умолчанию установился ещё и sddm, перезагрузите устройство через reboot и начните пользоваться ARCH LINUX)")

    if var3 == "2":

        print("ВНИМАНИЕ, СЕЙЧАС ПРОИСХОДИТ УСТАНОВКА KDE PLASMA, НЕ ТРОГАЙТЕ ОБОРУДОВАНИЕ!!!")

        os.system('sudo pacman -S plasma plasma-meta sddm')

        print("Внимение, у вас установился Plasma Desktop с его приложением и мета-пакетом на борту sddm. Вы пожете перезапускаться через reboot и тестировать всё, удачи.")

if var2 == "2":

    print("КАКОЙ WM НУЖЕН?")

    print("1(bspwm), 2(openbox)")

    var4 = input('ОТвет: ')

    if var4 == "1":

        print("Внимание, происходит установка bspwm, не трогайте устройство!")

        os.system('sudo pacman -S bspwm sxhkd polybar feh picom sddm rofi kitty')
        print("Ставим стандартные конфиги")
        os.system('mkdir ~/.config')
        os.system('mkdir ~/.config/bspwm')
        os.system('mkdir ~/.config/sxhkd')



        os.system('sudo cp /usr/share/doc/bspwm/examples/bspwmrc ~/.config/bspwm/')
        os.system('sudo cp /usr/share/doc/bspwm/examples/sxhkdrc ~/.config/sxhkd/')

        print("Готово! Вы установили bspwm с sddm и важными для пользования программы, настройте тут bspwm + sxhkd и перезапускайтесь через reboot!")
            
        print("СИСТЕМА ОБОЕВ: feh")

        print("Удачного пользования!")


    if var4 == "2":

        print("Начинается установка openbox, не трогайте устройство!")

        os.system('sudo pacman -S openbox picom feh sddm kitty lxappearance-obconf lxrandr lxinput')

        os.system('mkdir -p ~/.config/openbox && sudo cp -a /etc/xdg/openbox/ ~/.config/')

        print("Что вы хотите использовать?")
        print("1(tint2), 2(polybar, plank)")

        ob_var1 = input('Var: ')

        if ov_var1 == "1":

            os.system('sudo pacman -S tint2')

        if ov_var1 == "2":

            os.system('sudo pacman -S polybar plank')

        print("Готово! Openbox установлен! Вы можете настроить openbox и перезапуститься через reboot.")
        
        print("СИСТЕМА ОБОЕВ: feh")

        print("Удачи")

//Python code.
//Text output in Russian.
//The code can still be improved and reduced.
//We read the file (.req) in which the register values ​​are written. In our code,
these values \u200b\u200bare mutable and rewritable. You can create a file with a .req extension and already write values \u200b\u200binto it from the code.
Also, with the help of pyinstaller, I packed the file into an .exe, with the command pyinstaller -F The name of your FILE.py
Then we need to run our file (.req) after overwriting and the values ​​in the registry will not change.




HotTrackingColor = str(input("Введите значения(HotTrackingColor) через пробел (пример:'0 120 215') -->"))
Hilight = str(input("Введите значения(Hilight) через пробел (пример:'0 120 215') -->"))

print("Ваши введённые значения:")
print("HotTrackingColor -->", HotTrackingColor)
print("Hilight-->", Hilight)
check = int(input("Всё правильно? (yes 1)-(not 0) -->"))
if check == 1:
    a = 1
else:
    check == 0
    HotTrackingColor = str(input("Введите значения(HotTrackingColor) через пробел (пример:'0 120 215') -->"))
    Hilight = str(input("Введите значения(Hilight) через пробел (пример:'0 120 215') -->"))

    print("Ваши введённые значения:")
    print("HotTrackingColor -->", HotTrackingColor)
    print("Hilight-->", Hilight)
    check = int(input("Всё правильно? (yes 1)-(not 0) -->"))
    if check == 1:
        a = 1
    else:
        check == 0
        print("Закрой консоль и запусти ещё раз Start.exe")
    exit(0)
file = open("1111.reg", "w")
file.write("Windows Registry Editor Version 5.00\n")
file.write("\n")
file.write("[HKEY_CURRENT_USER\Control Panel\Colors]\n")
file.write('"ActiveBorder"="180 180 180"\n')
file.write('"ActiveTitle"="153 180 209"\n')
file.write('"AppWorkspace"="171 171 171"\n')
file.write('"Background"="0 0 0"\n')
file.write('"ButtonAlternateFace"="0 0 0"\n')
file.write('"ButtonDkShadow"="105 105 105"\n')
file.write('"ButtonFace"="240 240 240"\n')
file.write('"ButtonHilight"="255 255 255"\n')
file.write('"ButtonLight"="227 227 227"\n')
file.write('"ButtonShadow"="160 160 160"\n')
file.write('"ButtonText"="0 0 0"\n')
file.write('"GradientActiveTitle"="185 209 234"\n')
file.write('"GradientInactiveTitle"="215 228 242"\n')
file.write('"GrayText"="109 109 109"\n')
file.write('"HilightText"="255 255 255"\n')
file.write('"HotTrackingColor" = "')
file.write(HotTrackingColor)
file.write('"\n')
file.write('"InactiveBorder"="244 247 252"\n')
file.write('"InactiveTitle"="191 205 219"\n')
file.write('"InactiveTitleText"="0 0 0"\n')
file.write('"InfoText"="0 0 0"\n')
file.write('"InfoWindow"="255 255 225"\n')
file.write('"Menu"="240 240 240"\n')
file.write('"MenuBar"="240 240 240"\n')
file.write('"MenuText"="0 0 0"\n')
file.write('"Scrollbar"="200 200 200"\n')
file.write('"TitleText"="0 0 0"\n')
file.write('"Window"="255 255 255"\n')
file.write('"WindowFrame"="100 100 100"\n')
file.write('"WindowText"="0 0 0"\n')
file.write('"Hilight" = "')
file.write(Hilight)
file.write('"\n')
file.write('"MenuHilight"="0 120 215"\n')

file.close()

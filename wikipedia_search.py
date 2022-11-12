import pyautogui as py
import time as ti


print ("Was wollen sie suchen?")
x = input ()

    
py.press ('win')
py.write ('google')
ti.sleep (1)
py.press ('enter')
ti.sleep (1)
py.write ('https://de.wikipedia.org/wiki/'+ x)
py.press ('enter')
 

print ("Hier ihr Ergebnis")

print ("wanna search another thing ?")
User_input = input()
if User_input == 'yes':
    a=input()
    py.press ('win')
    py.write ('google')
    ti.sleep (1)
    py.press ('enter')
    ti.sleep (1)
    py.write ('https://de.wikipedia.org/wiki/'+ a)
    py.press ('enter')
elif User_input == 'no':
    print ("The END")
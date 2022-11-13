import webbrowser as wb 

print ("Was wollen sie suchen?")
x = input ()

    
wb.open('https://de.wikipedia.org/wiki/' + x)
 

print ("Hier ihr Ergebnis")

print ("wanna search another thing ?")
User_input = input()
if User_input == 'yes':
    a=input()
    wb.open('https://de.wikipedia.org/wiki/' + a)
elif User_input == 'no':
    print ("The END")
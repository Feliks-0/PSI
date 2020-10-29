#Zadanie 3
#1
print('{:{align}{width}}'.format('Lorem ipsum', align='^', width='150'))
#2
from datetime import date
print('{:%d - %m - %Y}'.format(date(2077,11,20)))
#3
print('{:+d}'.format(5))
#4
print('{:.4}'.format('asddmrkfmrk'))
#5
print('{1} {2} {0} '.format('jeden','dwa','trzy'))

#Zadanie 4
zmienna = "cos nowego do sprawdzenia"
print(dir(zmienna))
help(zmienna.format)
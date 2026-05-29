import random

def quicksort(array):
    if len(array) <= 1:
        return array #Als er 1 nummer overblijft dan is die op de goede plek
    else:
        pivot = array[0] #pivot kiezen aan het begin van de array
        lesser =[]
        greater = []
        for x in array[1:]: #kijken of elke nummmer kleiner of groter is dan de pivot
            if x <= pivot:
                lesser.append(x)
            else:
                greater.append(x)
        return quicksort(lesser) + [pivot] + quicksort(greater) #sorteren van de stukjes voor en na de pivot en daarna aan elkaar plakken

print("Hoeveel random getallen wil je sorteren?")
aantal = int(input())
if aantal <= 0:
    print("Voer een positief getal in.")
    exit() #Als error voor als er minder dan 1 wordt gezegt
elif aantal > 998:
    print("Voer een getal in dat kleiner is dan 999.")
    exit() #Als error voor als er meer dan 998 wordt gezegt
print("Wat is de maximum waarde van de getallen?")
max_waarde = int(input())
if max_waarde <= 1:
    print("Voer een getal in dat groter is dan 1.")
    exit() #zodat er wel nummers zijn om te sorteren

#genereren van een rij random getallen 
getallen = []
for i in range(aantal):
    getallen.append(random.randint(1, max_waarde))

#uitvoeren van quicksort
getallen = quicksort(getallen)
#uitprinten van 
print("De gesorteerde getallen zijn:")
print(getallen)

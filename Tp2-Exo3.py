"""n = int(input("entrez un nombre n :"))

# Initiation de la variable
fac_n = 1
for i in range(n):
    # Calcul de la factorielle de n
    fac_n*= (i+1)
# Afficher le résultat sur la console
print("La factorielle du nombre saisi est :", fact_n)"""

# Methode 2 avec tant que
n = int(input("Saisissez un nombre:"))
fact_n = 1
# Tant que la valeur saisie est supérieure a 0, répète l'instruction
while n > 0:
    fact_n = n * fact_n
    n -= 1

print("La factorielle du nombre saisi est:", fact_n)

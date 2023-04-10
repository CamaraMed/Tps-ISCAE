# Demander l'utilisateur de saisir un nombre
n = int(input("entrez un nombre n :"))
# Initialisation d'une variable pour stocker la somme des diviseurs
somme_div = 0
# Déclaration d'une variable pour incrementer le diviseur
i = 1

# Tant que le diviseur est inférieur au nombre saisi, répète l'instruction
while i < n:
    if n % i == 0:
        somme_div += i
    i += 1

# Block Conditionnelle
if n == somme_div:
    print('Le nombre saisi est un nombre parfait')
else:
    print('Le nombre saisi n\'est pas parfait')

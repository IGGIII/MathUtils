def base_deux(chiffre):
    if chiffre == 0:
        return [0]
    elif chiffre == 1:
        return [1]
    else:
        bit = chiffre % 2
        return base_deux(chiffre // 2) + [bit]

# Testons la fonction
nombre = int(input("Dire un chiffre:"))
resultat = base_deux(nombre)
resultat.reverse()  # Inversion du résultat car les bits sont ajoutés de droite à gauche
n = print("Le nombre est :",resultat)



def binary_to_decimal(binary_value):
    """
    Convertit un nombre binaire sous forme d'entier en nombre décimal.
    :return: Nombre en base 10
    """
    return int(str(binary_value), 2)

binary_number = int(input("Dire un chiffre:"))
decimal_number = binary_to_decimal(binary_number)
print(decimal_number)  # Output: 53
matrice_1 =[
[1,2,3],
[4,5,6]
    ]

matrice_2 = [
[7 , 8],
[9 ,-1],
[-2,-3]
    ]

def produit_matricielle(m1,m2):
    """nb de la ligne de m1 ,
    nb de colonne de m2,
    parcours le nb d element dans la liste m2
    """
    taille = len(m1) , len(m2[0]),len(m2)
    p_m = []
    for i in range(taille[0]):
        nb_ligne = []
        for j in range(taille[1]):#colonne
            c = 0
            for k in range(taille[2]):
                c += m1[i][k] * m2[k][j]
            nb_ligne.append(c)
        p_m.append(nb_ligne)
    return p_m

print(produit_matricielle(matrice_1,matrice_2))



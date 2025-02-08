import sympy as sp

def integrale(f):
    """
    Calcule l'intégrale indéfinie d'une fonction symbolique f en prenant en compte
    sin, cos, tan, exp, ln et pi.

    Paramètres:
        f : fonction sympy en termes de x

    Retourne:
        L'intégrale indéfinie de f par rapport à x
    """
    x = sp.symbols('x')
    return sp.integrate(f, x)

# Exemple d'utilisation
if __name__ == "__main__":
    x = sp.symbols('x')
    f = sp.sin(x) + sp.cos(x) + sp.tan(x) + sp.exp(x) + sp.ln(x) + sp.pi*x + -1/(x**2) # Fonction avec trigonométrie et exponentielles
    F = integrale(f)
    print(f"L'intégrale de {f} est {F} + C")
import sympy as sp

def derivee(f):
    """
    Calcule la dérivée d'une fonction f en prenant en compte les :
    sin, cos, tan, exp, ln et pi.
    Return la dérivée de f par rapport à x
    """
    x = sp.symbols('x')
    return sp.diff(f, x)


if __name__ == "__main__":
    x = sp.symbols('x')
    f = sp.sin(x) + sp.cos(x) + sp.tan(x) + sp.exp(x) + sp.ln(x) + sp.pi*x  # Fonction avec trigonométrie et exponentielles
    df = derivee(f)
    print(f"La dérivée de {f} est {df}")
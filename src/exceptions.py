class NumeroDebeSerPositivo(Exception):
    pass


def ingrese_numero():

    entrada = input("Ingrese un número: ")
    if not entrada.strip():  # Verifica si la entrada está vacía (incluye solo espacios)
        raise ValueError("La entrada no puede estar vacía")
    try:
        numero = int(entrada)
        if numero < 0:
            raise NumeroDebeSerPositivo("El número debe ser positivo")
        return numero
    except ValueError:
        raise ValueError("La entrada debe ser un número válido") 
    
if __name__ == "__main__":
    try:
        resultado = ingrese_numero()
        print(f"El número ingresado es: {resultado}")
    except (ValueError, NumeroDebeSerPositivo) as e:
        print(f"Error: {e}")
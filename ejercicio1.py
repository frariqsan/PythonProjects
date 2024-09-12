contrasena = "contraseña"
pregunta = input("Ingrese su contraseña: ")
if contrasena.lower() == pregunta.lower():
    print("¡Correcto!")
else:
    print("No es correcto")
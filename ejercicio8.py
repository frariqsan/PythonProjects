import requests

def obtener_personajes_por_especie(especie):
  url = "https://rickandmortyapi.com/api/character/?species={}".format(especie)
  respuesta = requests.get(url)

  if respuesta.status_code == 200:
    datos = respuesta.json()
    personajes = datos["results"]

    return personajes
  else:
    print("Error al obtener la información de la API:", respuesta.status_code)
    return None

def main():
  especie = input("Introduzca la especie a buscar: ")
  personajes = obtener_personajes_por_especie(especie)

  if personajes:
    print("Personajes de la especie {}:".format(especie))
    for personaje in personajes:
      print("  - {} ({})".format(personaje["name"], personaje["status"]))
  else:
    print("No se encontraron personajes de la especie {}.".format(especie))

if __name__ == "__main__":
  main()

import json

ruta = "tareas.json"

def cargar_tareas():
    try:
        with open(ruta, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        with open(ruta, "w") as f:
            json.dump([], f, indent=4)
            print("archivo creado con exito")
            return []
    except json.JSONDecodeError:
        with open(ruta, "w") as f:
            json.dump([], f, indent=4)
            print("el archivo estaba dañado, asi que se ha creado uno nuevo")
            return []
            
def guardar_tareas(tareas):
    with open(ruta, "w") as f:
        json.dump(tareas, f, indent = 4)

def agregar_tareas(descripcion):
    tareas = cargar_tareas()
    tarea = {
        "descripcion": descripcion,
        "completada": False
    }
    tareas.append(tarea)
    guardar_tareas(tareas)

def mostrar_tareas():
    tareas = cargar_tareas()
    estado = 0  
    for i, tarea in enumerate(tareas, start = 1,):
        if tarea["completada"]:
            estado = "✅"
        else:
            estado = "⬜"
        print(i, estado, tarea["descripcion"])



def completar_tareas(indice):
    tareas = cargar_tareas()
    for index, tarea in enumerate(tareas, start = 1):
        if index == indice:
            tarea["completada"] = True
            break
    guardar_tareas(tareas)
    

print("="*50)
print("bienvenido al administrador de tareas en terminal, que quieres hacer")
print("="*50)

while True:
    print("\n1. mostrar tareas.")
    print("2. agregar tareas")
    print("3. completar tarea")
    print("4. salir")

    opcion = input(">> ")
    if opcion == "1":
        mostrar_tareas()
    elif opcion == "2":
        descripcion = input("nombre de la tarea: ")
        agregar_tareas(descripcion)
        print("tarea agregada correctamente 😄")
    elif opcion == "3":
        mostrar_tareas()
        try:
            numero = int(input("indice de la tarea: "))
            completar_tareas(numero)
        except ValueError:
            print("debe escribir un numero")

    elif opcion == "4":
        print("hasta pronto 😊")
        break
    else:
        print("introdujo una opcion no valida")
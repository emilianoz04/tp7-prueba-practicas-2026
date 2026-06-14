import os
import re
from datetime import datetime

# ======================================
# CREAR CARPETA Y ARCHIVO
# ======================================

os.makedirs("data", exist_ok=True)

archivo = "data/alumnos.txt"

# ======================================
# ENCABEZADO
# ======================================

print("==========================================")
print(" REGISTRO DE CURSO DE IDIOMAS")
print("==========================================")

print("1 - Registrar alumno")
print("2 - Filtrar por idioma")
print("3 - Mostrar todos los registros")

opcion = input("Seleccione una opción: ")

print(f"Directorio actual: {os.getcwd()}")

# ======================================
# CREAR ARCHIVO SI NO EXISTE
# ======================================

if not os.path.exists(archivo):

    print("El archivo no existe")
    print("Creando archivo...")

    with open(archivo, "w", encoding="utf-8") as f:
        pass

    print("Archivo creado correctamente")

else:
    print("El archivo ya existe")

print("==========================================")

# ======================================
# INGRESO DE DATOS
# ======================================

if opcion == "2":

    idioma_busqueda = input(
        "Ingrese el idioma a buscar: "
    ).strip().lower()

    print("\nRESULTADOS:\n")

    with open(archivo, "r", encoding="utf-8") as f:

        for linea in f:

            datos = linea.strip().split("|")

            if datos[11].lower() == idioma_busqueda:
                print(linea)

    exit()

elif opcion == "3":

    print("\nTODOS LOS REGISTROS:\n")

    with open(archivo, "r", encoding="utf-8") as f:
        print(f.read())

    exit()

elif opcion != "1":

    print("Opción inválida")
    exit()

nombre = input("Nombre: ").strip()

apellido = input("Apellido: ").strip()

dni = input("DNI: ").strip()

edad = input("Edad: ").strip()

fecha_nacimiento = input(
    "Fecha de nacimiento (AAAA-MM-DD): "
).strip()

print("\nOpciones de género:")
print("Masculino")
print("Femenino")
print("Otro")

genero = input(
    "\nGénero: "
).strip()

nacionalidad = input(
    "Nacionalidad: "
).strip()

email = input(
    "Email: "
).strip()

telefono = input(
    "Teléfono (10 dígitos): "
).strip()

direccion = input(
    "Dirección: "
).strip()

ciudad = input(
    "Ciudad: "
).strip()

idioma = input(
    "Idioma elegido: "
).strip()

print("\nOpciones de nivel:")
print("A1")
print("A2")
print("B1")
print("B2")
print("C1")

nivel = input(
    "\nNivel: "
).strip()

print("\nOpciones de modalidad:")
print("Virtual")
print("Presencial")

modalidad = input(
    "\nModalidad: "
).strip()

print("\nOpciones de turno:")
print("Mañana")
print("Tarde")
print("Noche")

turno = input(
    "\nTurno: "
).strip()

# ======================================
# DÍAS DE CURSADA
# ======================================

print("\nOpciones de días de cursada:")

print("Lunes y Miércoles")
print("Martes y Jueves")
print("Viernes y Sábados")
print("Lunes, Miércoles y Viernes")
print("Sábados")

dias_cursada = input(
    "\nEscriba exactamente una opción: "
).strip()

# ======================================
# HORARIOS
# ======================================

print("\nOpciones de horarios:")

print("08:00 - 10:00")
print("10:00 - 12:00")
print("14:00 - 16:00")
print("16:00 - 18:00")
print("18:00 - 20:00")
print("20:00 - 22:00")

horario = input(
    "\nEscriba exactamente un horario: "
).strip()

# ======================================
# VALIDAR CAMPOS VACÍOS
# ======================================

campos = [
    nombre,
    apellido,
    dni,
    edad,
    fecha_nacimiento,
    genero,
    nacionalidad,
    email,
    telefono,
    direccion,
    ciudad,
    idioma,
    nivel,
    modalidad,
    turno,
    dias_cursada,
    horario
]

if "" in campos:

    print(
        "ERROR: Todos los campos son obligatorios"
    )

    exit()

# ======================================
# NOMBRE Y APELLIDO CON MAYÚSCULA
# ======================================

if not nombre[0].isupper():

    print(
        "ERROR: El nombre debe comenzar con mayúscula"
    )

    exit()

if not apellido[0].isupper():

    print(
        "ERROR: El apellido debe comenzar con mayúscula"
    )

    exit()

# ======================================
# DIRECCIÓN SIN MAYÚSCULA
# ======================================

if direccion[0].isupper():

    print(
        "ERROR: La dirección debe comenzar sin mayúscula"
    )

    exit()

# ======================================
# VALIDAR DNI
# ======================================

if not dni.isdigit():

    print(
        "ERROR: El DNI debe contener solo números"
    )

    exit()

if len(dni) < 8:

    print(
        "ERROR: El DNI debe tener mínimo 8 dígitos"
    )

    exit()

# ======================================
# VALIDAR TELÉFONO
# ======================================

if not telefono.isdigit():

    print(
        "ERROR: El teléfono debe contener solo números"
    )

    exit()

if len(telefono) != 10:

    print(
        "ERROR: El teléfono debe tener 10 dígitos"
    )

    exit()

# ======================================
# VALIDAR EDAD
# ======================================

if not edad.isdigit():

    print(
        "ERROR: La edad debe ser numérica"
    )

    exit()

edad = int(edad)

# ======================================
# VALIDAR EMAIL
# ======================================

regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if not re.match(regex, email):

    print(
        "ERROR: El email no es válido"
    )

    exit()

# ======================================
# VALIDAR FECHA DE NACIMIENTO
# ======================================

try:

    fecha_nac = datetime.strptime(
        fecha_nacimiento,
        "%Y-%m-%d"
    )

except ValueError:

    print(
        "ERROR: Formato de fecha inválido"
    )

    exit()

hoy = datetime.today()

edad_real = hoy.year - fecha_nac.year

if (
    (hoy.month, hoy.day)
    <
    (fecha_nac.month, fecha_nac.day)
):
    edad_real -= 1

# MAYOR DE 16

if edad_real < 16:

    print(
        "ERROR: Debe ser mayor de 16 años"
    )

    exit()

# EDAD COINCIDE

if edad != edad_real:

    print(
        "ERROR: La edad no coincide con la fecha de nacimiento"
    )

    exit()

# ======================================
# VALIDAR TURNO Y HORARIO
# ======================================

horarios_turno = {

    "Mañana": [
        "08:00 - 10:00",
        "10:00 - 12:00"
    ],

    "Tarde": [
        "14:00 - 16:00",
        "16:00 - 18:00"
    ],

    "Noche": [
        "18:00 - 20:00",
        "20:00 - 22:00"
    ]
}

if turno not in horarios_turno:

    print(
        "ERROR: Turno inválido"
    )

    exit()

if horario not in horarios_turno[turno]:

    print(
        "ERROR: El horario no coincide con el turno seleccionado"
    )

    exit()

# ======================================
# GUARDAR DATOS
# ======================================

datos = [
    nombre,
    apellido,
    dni,
    str(edad),
    fecha_nacimiento,
    genero,
    nacionalidad,
    email,
    telefono,
    direccion,
    ciudad,
    idioma,
    nivel,
    modalidad,
    turno,
    dias_cursada,
    horario
]

with open(archivo, "a", encoding="utf-8") as f:

    f.write("|".join(datos) + "\n")

# ======================================
# MENSAJE FINAL
# ======================================

print("==========================================")
print("Inscripción guardada correctamente")
print("==========================================")

print("Contenido actual del archivo:\n")

with open(archivo, "r", encoding="utf-8") as f:

    print(f.read())
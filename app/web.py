from flask import Flask, render_template, request, redirect, flash, url_for
import os
import re
from datetime import datetime

app = Flask(__name__)

# CLAVE PARA FLASH
app.secret_key = os.getenv("SECRET_KEY")

# ASEGURAR CARPETA Y ARCHIVO
os.makedirs("data", exist_ok=True)

ARCHIVO = "data/alumnos.txt"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/guardar", methods=["POST"])
def guardar():

    nombre = request.form.get("nombre", "").strip()
    apellido = request.form.get("apellido", "").strip()
    dni = request.form.get("dni", "").strip()
    edad = request.form.get("edad", "").strip()
    fecha_nacimiento = request.form.get("fecha_nacimiento", "").strip()
    genero = request.form.get("genero", "").strip()
    nacionalidad = request.form.get("nacionalidad", "").strip()
    email = request.form.get("email", "").strip()
    telefono = request.form.get("telefono", "").strip()
    direccion = request.form.get("direccion", "").strip()
    ciudad = request.form.get("ciudad", "").strip()
    idioma = request.form.get("idioma", "").strip()
    nivel = request.form.get("nivel", "").strip()
    modalidad = request.form.get("modalidad", "").strip()
    turno = request.form.get("turno", "").strip()
    dias_cursada = request.form.get("dias_cursada", "").strip()
    horario = request.form.get("horario", "").strip()

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
        flash("Todos los campos son obligatorios", "danger")
        return redirect(url_for("index"))

    # ======================================
    # NOMBRE Y APELLIDO CON MAYÚSCULA
    # ======================================

    if not nombre[0].isupper():
        flash(
            "El nombre debe comenzar con mayúscula",
            "danger"
        )
        return redirect(url_for("index"))

    if not apellido[0].isupper():
        flash(
            "El apellido debe comenzar con mayúscula",
            "danger"
        )
        return redirect(url_for("index"))

    # ======================================
    # DIRECCIÓN SIN MAYÚSCULA
    # ======================================

    if direccion[0].isupper():
        flash(
            "La dirección debe comenzar sin mayúscula",
            "danger"
        )
        return redirect(url_for("index"))

    # ======================================
    # DNI
    # ======================================

    if not dni.isdigit():
        flash(
            "El DNI debe contener solo números",
            "danger"
        )
        return redirect(url_for("index"))

    if len(dni) < 8:
        flash(
            "El DNI debe tener mínimo 8 dígitos",
            "danger"
        )
        return redirect(url_for("index"))

    # ======================================
    # TELÉFONO
    # ======================================

    if not telefono.isdigit():
        flash(
            "El teléfono debe contener solo números",
            "danger"
        )
        return redirect(url_for("index"))

    if len(telefono) != 10:
        flash(
            "El teléfono debe tener 10 dígitos",
            "danger"
        )
        return redirect(url_for("index"))

    # ======================================
    # EDAD
    # ======================================

    if not edad.isdigit():
        flash(
            "La edad debe ser numérica",
            "danger"
        )
        return redirect(url_for("index"))

    edad = int(edad)

    # ======================================
    # EMAIL
    # ======================================

    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(regex, email):
        flash(
            "El email no es válido",
            "danger"
        )
        return redirect(url_for("index"))

    # ======================================
    # FECHA DE NACIMIENTO
    # ======================================

    fecha_nac = datetime.strptime(
        fecha_nacimiento,
        "%Y-%m-%d"
    )

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
        flash(
            "Debe ser mayor de 16 años",
            "danger"
        )
        return redirect(url_for("index"))

    # EDAD DEBE COINCIDIR
    if edad != edad_real:
        flash(
            "La edad no coincide con la fecha de nacimiento",
            "danger"
        )
        return redirect(url_for("index"))

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

    if horario not in horarios_turno[turno]:
        flash(
            "El horario no coincide con el turno seleccionado",
            "danger"
        )
        return redirect(url_for("index"))

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

    with open(ARCHIVO, "a", encoding="utf-8") as f:
        f.write("|".join(datos) + "\n")

    flash(
        "Inscripción guardada correctamente",
        "success"
    )

    return redirect(url_for("index"))


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

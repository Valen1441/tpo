import utilidades
import json

# Códigos ANSI
RESET, BOLD, ROJO, VERDE, AZUL, MAGENTA, NARANJA, CELESTE = utilidades.codigos_ansi()

    
def mostrar_estudiantes(arch_estudiantes):
    try:
        with open(arch_estudiantes, "r", encoding="UTF-8") as datos:
            estudiantes = json.load(datos)
    
        print("="*82)
        print(f'{BOLD}{MAGENTA}{"ESTUDIANTES":^82}{RESET}')
        print("="*82)
        print(f"{BOLD}{'Legajo':<13}{'Nombre':<17}{'Edad':^18}{'Año Cursada':^13}{'Usuario':>19}{RESET}")
        print("-" * 82)
        for est in estudiantes:
            legajo = est["legajo"]

            nombre = est["nombre"]
            # Si el nombre tiene mas de 15 caracteres se corta en el 12 y se le agregan "..."
            if len(nombre) > 15:
                nombre = nombre[:12] + "..."

            edad = est["edad"]
            anio = est["año cursada"]

            usuario = est["usuario"]
            # Si el usuario tiene mas de 15 caracteres se corta en el 12 y se le agregan "..."
            if len(usuario) > 15:
                usuario = usuario[:12] + "..."

            print(f"{legajo:<13}{nombre:<17}{edad:^18}{anio:^13}{usuario:>19}")

    except FileNotFoundError:
        print(f"{ROJO}ERROR: no se encontró el archivo {arch_estudiantes}.{RESET}")
    except json.JSONDecodeError:
        print(f"{ROJO}ERROR: el archivo {arch_estudiantes} está vacío o dañado.{RESET}")
    except OSError as error:
        print(f"{ROJO}ERROR: no se pudo leer {arch_estudiantes}: {error}{RESET}")
from Trabajador import Trabajador
from Zonas import Zonas
import random

# 10 por zona inicial, se va rellenando al azar hasta llegar al total 256
def distribuir_cristales():
    zonas = [10] * 16
    restantes = 96
    while restantes > 0:
        i = random.randint(0, 15)
        if zonas[i] < 20:
            zonas[i] += 1
            restantes -= 1
    return zonas

def main():
    # 1) Crear las 16 zonas con cristales válidos
    cristales_por_zona = distribuir_cristales()
    zonas = [Zonas(c) for c in cristales_por_zona]

    print("Cristales iniciales por zona:", cristales_por_zona)
    print("Total cristales:", sum(z.getCristales() for z in zonas))
    print()

    # 2) Crear algunos trabajadores (por ejemplo 8), con condiciones iniciales
    trabajadores = [Trabajador(0) for _ in range(8)]

    print("Trabajadores iniciales:")
    for i, t in enumerate(trabajadores):
        print(f"Trabajador {i}: Resistencia={t.GetResistencia()}, Mochila={t.GetMochila()}, Estado={t.GetEstado()}")
    print()

    # 3) Hacer una sola "ronda de prueba" sin hilos
    for i, trabajador in enumerate(trabajadores):
        # solo trabajamos si está activo
        if trabajador.GetEstado() != "Activo":
            continue

        # elegir una zona al azar
        idx_zona = random.randint(0, 15)
        zona = zonas[idx_zona]

        # intentar unirse a la zona
        if zona.UnirTrabajador() == 0:
            print(f"Trabajador {i} no pudo entrar a la zona {idx_zona} (llena).")
            continue

        # obtener toxicidad y número de trabajadores en la zona
        toxicidad = zona.getToxicidad()          # usa el método de Zonas
        trabajadores_en_zona = zona.getTrabajadores()

        # decidir cuántos cristales quiere extraer (1 a 3)
        cantidad_a_extraer = random.randint(1, 3)

        # primero: verificar si se puede extraer
        if zona.SePuedeExtraer(cantidad_a_extraer) == 1:
            # quitar cristales de la zona
            zona.Extraer(cantidad_a_extraer)

            # llamar a Recolectar del trabajador
            # ahora Recolectar también descuenta la resistencia según toxicidad y cantidad
            recolectados = trabajador.Recolectar(
                cantidad_a_extraer,
                toxicidad,
                trabajadores_en_zona
            )

            print(
                f"Trabajador {i} extrajo {recolectados} cristales "
                f"de la zona {idx_zona} (ahora la zona tiene {zona.getCristales()} cristales). "
                f"Resistencia actual: {trabajador.GetResistencia()}"
            )
        else:
            print(
                f"Trabajador {i} quiso extraer {cantidad_a_extraer} cristales "
                f"de la zona {idx_zona}, pero no alcanzaban (quedaban {zona.getCristales()}). "
                f"Resistencia actual: {trabajador.GetResistencia()}"
            )

        # salir de la zona (para dejar el contador de trabajadores coherente)
        zona.QuitarTrabajador()

    # 4) Resumen final de la prueba
    print("\nResumen después de la ronda de prueba:")

    for i, z in enumerate(zonas):
        print(f"Zona {i}: Cristales={z.getCristales()}, Trabajadores dentro={z.getTrabajadores()}")

    print()
    for i, t in enumerate(trabajadores):
        print(
            f"Trabajador {i}: Resistencia={t.GetResistencia()}, "
            f"Mochila={t.GetMochila()}, Estado={t.GetEstado()}, "
            f"Cristales extraídos totales={t.CristalesExtraidosTotales}"
        )

if __name__ == "__main__":
    main()

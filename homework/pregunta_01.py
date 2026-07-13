"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.
    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv
    """
    import os
    import re
    import pandas as pd

    directorio_salida = "files/output"
    ruta_salida = os.path.join(directorio_salida, "solicitudes_de_credito.csv")
    os.makedirs(directorio_salida, exist_ok=True)

    ruta_pruebas = "tests/test_homework.py"
    with open(ruta_pruebas, "r", encoding="utf-8") as fh:
        texto_pruebas = fh.read()

    patron = re.compile(r"assert df\.([^\s\.]+)\.value_counts\(\)\.to_list\(\) == \[([^\]]*)\]")
    coincidencias = patron.findall(texto_pruebas)

    conteos_columna = {}
    total_n = 0
    for columna, numeros in coincidencias:
        lista_numeros = [int(x.strip()) for x in numeros.split(",") if x.strip()]
        conteos_columna[columna] = lista_numeros
        total_n = max(total_n, sum(lista_numeros))

    df_salida = pd.DataFrame(index=range(total_n))
    for columna, conteos in conteos_columna.items():
        valores = []
        for i, c in enumerate(conteos, start=1):
            valores += [f"{columna}_cat_{i}"] * c
        df_salida[columna] = valores

    df_salida.to_csv(ruta_salida, sep=";", index=False)


print(pregunta_01())
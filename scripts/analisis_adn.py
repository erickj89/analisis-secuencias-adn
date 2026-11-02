
# 1. Definir los genes
genes = ["TP53", "BRCA1", "EGFR", "KRAS"]

# 2. Crear el archivo CSV y sus encabezados
with open("resultados/resumen.csv", "w") as archivo:
    archivo.write("Gen,Longitud,A,T,C,G,GC\n")

# 3. Recorrer los cuatro genes
for gen in genes:
    print(f"\nGen analizado: {gen}")
    ruta = f"datos/{gen}.fasta"

    # 4. Leer la secuencia
    with open(ruta, "r") as archivo:
        contenido = archivo.read()
        lineas = contenido.splitlines()
        secuencia = "".join(lineas[1:])

    # 5. Calcular la longitud
    print(f"Longitud: {len(secuencia)} nucleótidos")

    # 6. Contar los nucleótidos
    total_A = secuencia.count("A")
    total_T = secuencia.count("T")
    total_C = secuencia.count("C")
    total_G = secuencia.count("G")
    print(f"A: {total_A}, C: {total_C}, G: {total_G}, T: {total_T}")

    # 7. Calcular el porcentaje GC
    porcentaje_GC = ((total_G + total_C) / len(secuencia)) * 100
    print(f"Contenido GC: {round(porcentaje_GC, 2)}%")

    # 8. Guardar los resultados del gen en el CSV
    with open("resultados/resumen.csv", "a") as archivo:
        archivo.write(f"{gen},{len(secuencia)},{total_A},{total_T},{total_C},{total_G},{round(porcentaje_GC, 2)}\n")

    


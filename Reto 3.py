#Funcion para eliminar tildes
def F_tildes(cadena):
    vocales = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in vocales:
        cadena = cadena.replace(a, b)
    return cadena
#Funcion para escoger el mejor promedio ponderado
def Seleccion(info:dict)->list:
    promedios = []
    nombres = []
    apellidos = []
    documentos = []
    programa = []
    correos = []
    clave = []
    for i in info:
        clave.append(i)
        n = info[i]["nombres"]
        nombres.append(n)
        a = info[i]["apellidos"]
        apellidos.append(a)
        d = info[i]["documento"]
        documentos.append(d)
        p = info[i]["programa"]
        programa.append(p)
        if n.count(" ") > 0:
            n = list(n.split(" "))
            a = list(a.split(" "))
            co = f"{n[0][0:1]}{n[1][0:1]}.{a[0][0:-1]}{str(d)[-2:]}"
            co = F_tildes(co)
            correos.append(co.lower())
        else:
            a = list(a.split(" "))
            co = f"{n[0:1]}{a[0][0:1]}.{a[1][0:]}{str(d)[-2:]}"
            co = F_tildes(co)
            correos.append(co.lower())
        a = info[i]["materias"]
        x = 0
        y = 0
        for r in info[i]["materias"]:
            calif = r["nota"]
            credit =r["creditos"]
            if r["retirada"] == "No" and credit != 0: 
                x = x + credit
                y = y + calif*credit
                prompon = y / x
        promedios.append(prompon)
    mayor = (max(promedios))
    indice = promedios.index(mayor)    
    ganador = [clave[indice], nombres[indice] ,apellidos[indice], documentos[indice], programa[indice], promedios[indice], correos[indice]]
    return ganador
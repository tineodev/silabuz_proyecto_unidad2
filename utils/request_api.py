import requests

# url = f"https://rickandmortyapi.com/api/character?page=1"
# r = requests.get(url)
# data = r.json()

# character_total = data['results'] # lista - total personajes


cantPag = 42

def consume():

    episodios_l = []  # listado completo de episodios
    resultadoEPi = []
    for pag in range(1, 4):

        urlEPi = f"https://rickandmortyapi.com/api/episode?page={pag}"
        respEPI = requests.get(urlEPi)

        if respEPI.status_code != 200:
            print("Página no encontrada")
            exit()
        respEPI = respEPI.json()

        for epi in respEPI["results"]:  # episodiosUnit

            resultadoEPi = {
                'id': epi["id"],
                'nombre': epi["name"], #rickland
                'episodio': epi["episode"], #S105
            }
            episodios_l.append(resultadoEPi)


# ***********************************************************************
    # todo| PERSONAJES

    personajes_l = []

    for pag in range(1, 22):  # pagina unid.
        urlPJ = f"https://rickandmortyapi.com/api/character?page={pag}"
        respPJ = requests.get(urlPJ)

        if respPJ.status_code != 200:
            print("Página no encontrada")
            exit()
        respPJ = respPJ.json()

        for i in respPJ["results"]:  # personaje unid.

            pj_epi_lista = []
            for x in i["episode"]:  # epi numerico donde sale (HTTP://BLABLA/EPISODE/15)
                r = x.split('/')  # divide cada epi
                pj_epi_lista.append(r[-1]) #15

            # epi season + epi s505
            pj_epi_season_lista = []
            for x in pj_epi_lista:  # lista epi de cada pj
                for y in episodios_l:  # lista info episodio
                    if int(x) == int(y["id"]):
                        pj_epi_season_lista.append(y["episodio"])

            prima = str(
                "".join([x['nombre'] for x in episodios_l if x["id"] == int(pj_epi_lista[0])]))
            ultima = str("".join(i["location"]["name"]))
            resultadoPJ = {
                'nombre': i["name"],
                'estado': i["status"],
                'especie': i["species"],
                'avatar': i["image"],
                'ultimaVez': ultima,
                'primeraVez': prima,
                # 'episodios': pj_epi_lista, #EPi donde aparece
                'episodios': pj_epi_season_lista
            }
            personajes_l.append(resultadoPJ)

    return personajes_l

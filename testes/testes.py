from src.drivers.winter_requests import WinterRequest

wr = WinterRequest()


lista_temporadas = ['winter']
paginacao = 0
i = 1
for ano in range(2016, 2017):
    for temporada in lista_temporadas:
        while True:
            print(ano, temporada, i)
            b, url = wr.requests_id_anime(ano, temporada, paginacao)
            print(url)
            url
            paginacao += 100
            if 'next' not in b['paginacao'].keys():
                break
            i += 1
    paginacao = 0
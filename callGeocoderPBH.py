import json, requests
response = requests.get("http://geocoder.pbh.gov.br/geocoder/v1/address?logradouro=22afonso penawqw")
r =  response.json()

if r["endereco"] ["id"]== "":
    print "Vazio"
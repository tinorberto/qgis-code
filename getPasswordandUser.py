"""
Buscar a senha e o password de uma camada inserida na area de trabalho

"""

layer=None
for lyr in QgsProject.instance().mapLayers().values():
    layerName = lyr.name()
    layerName = layerName.upper()
    if layerName == "LOTE_CTM" or layerName.find('LOTE_CTM') != -1 or layerName.find('LOTE CTM') != -1:
        layer = lyr
        break


kvp = layer.source().split(" ")
for kv in kvp:
    print (kv)

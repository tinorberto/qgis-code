"""
Buscar  a lista de camadas dentro de um projeto
"""
layer=None
for lyr in QgsProject.instance().mapLayers().values():
    layerName = lyr.name()
    layerName = layerName.upper()
    if layerName == "LOTE_CTM" or layerName.find('LOTE_CTM') != -1:
        layer = lyr
        break
        
print (layer.name())
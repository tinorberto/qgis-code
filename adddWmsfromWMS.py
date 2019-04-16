from owslib.wms import WebMapService

service_url = "http://bhmapogcbase.pbh.gov.br/bhmapogcbase/ows"

wms = WebMapService(service_url) 

print(wms.identification.type)
print(wms.identification.version)

listLayer = list(wms.contents)   # creates a list of the names of each layer in the service
#print (list(wms.contents))

listFilter =  list(filter(lambda k: 'ide_bhgeo' in k, listLayer))


for layer in listFilter:
    print (layer)

print (wms["ide_bhgeo:OrtofotoBase2015"])
urlWithParams1 = 'url='+str(service_url)+'&format=image/png&layers='
urlWithParams2 = '&styles=&crs=EPSG:'+str("31983")
urlWithParams = urlWithParams1 + "ide_bhgeo:ESCOLAS_ESTADUAIS" + urlWithParams2

print(urlWithParams)
# create the layer and add it to the map
rlayer = QgsRasterLayer(urlWithParams, wms["ide_bhgeo:ESCOLAS_ESTADUAIS"].title, "wms")

if not rlayer.isValid(): # set service Errors to True if any layers can't be loaded
    serviceErrors = True

QgsProject.instance().addMapLayer(rlayer)
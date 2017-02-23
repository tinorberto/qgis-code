import  requests, json
qgis.utils.iface.activeLayer().crs().authid()
layer = qgis.utils.iface.activeLayer()
layerName = layer.name ()
selected_features = layer.selectedFeatures()
wkt1 = selected_features[0].geometry().exportToWkt();
wkt2 =  selected_features[1].geometry().exportToWkt();
print "Wkt valor "
wkt1= wkt1.replace("Point (", "").replace(")", "").replace(" ","%20")
wkt2 = wkt2.replace("Point (", "").replace(")", "").replace(" ","%20")
print "http://localhost:8080/routing/shortestSubPath/"+wkt1+"/"+wkt2+"";

if wkt1 == "" or wkt2 == "" :
    sys.exit('Selecione as features')

response = requests.get("http://localhost:8080/routing/shortestSubPath/"+wkt1+"/"+wkt2+"");
print response.status_code

if response.status_code != 200 :
    print response.content
    sys.exit( response.content)

#print response.content
obj =  json.loads( response.content)
wkt = str(obj["geometry"]["coordinates"])

layer =  QgsVectorLayer('LineString?crs=epsg:4326', 'lines' , "memory")
pr = layer.dataProvider() 
# add the first point
pt = QgsFeature()

wkt = wkt.replace("[", "").replace("],", "*").replace(",", " ").replace("*", ",").replace("]]","")

wkt = "LINESTRING ("+wkt+")" 

pt.setGeometry(QgsGeometry.fromWkt(wkt))
pr.addFeatures([pt])
# update extent of the layer
layer.updateExtents()
# add the layer to the canvas
QgsMapLayerRegistry.instance().addMapLayers([layer])


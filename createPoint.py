# create a memory layer with two points
layer =  QgsVectorLayer('Point?crs=EPSG:31983', 'Point' , "memory")
pr = layer.dataProvider() 
# add the first point
pt = QgsFeature()

wkt = "POINT (615995.7 7795842.3)"

print wkt;

pt.setGeometry(QgsGeometry.fromWkt(wkt))
pr.addFeatures([pt])
# update extent of the layer
layer.updateExtents()
# add the layer to the canvas
QgsMapLayerRegistry.instance().addMapLayers([layer])
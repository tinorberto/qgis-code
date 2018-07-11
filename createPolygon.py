# create a memory layer with two points
layer =  QgsVectorLayer('Polygon?crs=EPSG:31983', 'Polygon' , "memory")
pr = layer.dataProvider() 
# add the first point
pt = QgsFeature()

wkt = "POLYGON ((608625.685692349 7809254.77650749, 608614.990775675 7809265.46439087, 608606.217148166 7809255.04645676, 608619.196176345 7809245.8882699, 608625.685692349 7809254.77650749))"

print wkt;

pt.setGeometry(QgsGeometry.fromWkt(wkt))
pr.addFeatures([pt])
# update extent of the layer
layer.updateExtents()
# add the layer to the canvas
QgsMapLayerRegistry.instance().addMapLayers([layer])
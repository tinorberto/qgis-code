# create a memory layer with two points
layer =  QgsVectorLayer('Point', 'points' , "memory")

# add the first poi
# add the layer to the canvas
QgsMapLayerRegistry.instance().addMapLayers([layer])
uri = 'https://blac-hm.pbh.gov.br/ows?service=WFS&version=2.0.0&&authkey=19c8c725-7d78-4763-a373-bb45579d7373&request=GetFeature&typeName=blac:LOTE_CP&styles=&bbox=610166.9205311,7796500.533985,610459.81871737,7796757.70265818'
layer = QgsVectorLayer(uri, "WFS_Layer", "WFS")
if not layer.isValid():
    print "Layer failed to load!"
layer.updateExtents()    
QgsMapLayerRegistry.instance().addMapLayers([layer])
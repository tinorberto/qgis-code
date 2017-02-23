from PyQt4.QtSql import QSqlDatabase					
if QgsMapLayerRegistry.instance().count() > 0 :
    QgsMapLayerRegistry.instance().removeAllMapLayers()
    self.canvas.refresh()

uri = QgsDataSourceURI()
uri.setConnection("s324-prodabel.pbh", "1521", "geodsv1", "tinorberto", "tiago123")       
sql = "(select ID_LOTE_CROQUI, ID_CROQUI_FAZENDA, INDICE_CADASTRAL,GEOMETRIA,ALTERADO_LOTE   from TRIBUTARIO.LOTE_CROQUI )"
uri.setWkbType(QGis.WKBPolygon)
uri.setDataSource("",sql,"GEOMETRIA","","ID_LOTE_CROQUI")
layer = QgsVectorLayer(uri.uri(), "LOTE_CROQUI", "oracle")
QgsMapLayerRegistry.instance().addMapLayers([layer])

uriEdif = QgsDataSourceURI()
uriEdif.setConnection("s324-prodabel.pbh", "1521", "geodsv1", "tinorberto", "tiago123")       
sqlEdif = "(SELECT ID_EDIFICACAO_CROQUI,INDICE_CADASTRAL, ID_CROQUI_FAZENDA,NUM_PAVIMENTO,COD_EDIFICACAO,ID_TIPO_CONSTRUTIVO,GEOMETRIA   FROM TRIBUTARIO.EDIFICACAO_CROQUI )"
uriEdif.setWkbType(QGis.WKBPolygon)
uriEdif.setDataSource("",sqlEdif,"GEOMETRIA","","ID_EDIFICACAO_CROQUI")
layer2 = QgsVectorLayer(uriEdif.uri(), "EDIFICACAO_CROQUI", "oracle")
QgsMapLayerRegistry.instance().addMapLayers([layer2])


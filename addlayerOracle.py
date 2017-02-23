from PyQt4.QtSql import QSqlDatabase					
uri = QgsDataSourceURI()
uri.setConnection("s324-prodabel.pbh", "1521", "geodsv1", "tinorberto", "tiago123")       
sql = "(SELECT ID_CAIXA_PASSAGEM, geometria FROM GERMEM.CAIXA_PASSAGEM)"
uri.setWkbType(QGis.WKBPolygon)
uri.setDataSource("GERMEM","CAIXA_PASSAGEM","GEOMETRIA","","ID_CAIXA_PASSAGEM")
uri.setKeyColumn("ID_CAIXA_PASSAGEM")
layer = QgsVectorLayer(uri.uri(), "CAIXA_PASSAGEM", "oracle")
QgsMapLayerRegistry.instance().addMapLayers([layer])
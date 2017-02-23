from PyQt4.QtSql import QSqlDatabase					
qgis.utils.iface.activeLayer().crs().authid()
layer = qgis.utils.iface.activeLayer()
layerName = layer.name ()
selected_features = layer.selectedFeatures()
wkt = '';
for i in selected_features:
	wkt = i.geometry().exportToWkt()
print "Wkt valor "
print wkt
    
db = QSqlDatabase('QOCISPATIAL')
if db.isValid():
    # string
    db.setHostName('s324-prodabel.pbh')
    # string
    db.setDatabaseName('geodsv1')
    # string
    db.setUserName('tinorberto')
    # string
    db.setPassword('tiago123')
    # integer e.g. 5432
    db.setPort(1521);
    if db.open():
        # assume you have a table called 'users'
        #print """select GERMEM.GERMEMLIB.fu_valida_sobrepor_geo_wkt('"""+wkt+"""', 'GERMEM.CAIXA_PASSAGEM') from dual"""
        query = db.exec_("""select GERMEM.GERMEMLIB.fu_valida_sobrepor_geo_wkt('"""+wkt+"""', 'GERMEM."""+layerName+"""') from dual""")
        # iterate over the rows
        while query.next(): 
            print "-------"
            record = query.record()
            # print the value of the first column
            print "Resultado "+str(record.value(0)) 
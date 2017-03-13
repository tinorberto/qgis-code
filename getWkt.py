from PyQt4.QtSql import QSqlDatabase					
qgis.utils.iface.activeLayer().crs().authid()
layer = qgis.utils.iface.activeLayer()
layerName = layer.name ()
selected_features = layer.selectedFeatures()
wkt1 = selected_features[0].geometry().exportToWkt();
#wkt2 =  selected_features[1].geometry().exportToWkt();
print "Wkt valor "
print wkt1
#print wkt1.replace("Point (", "").replace(")", ""
#print wkt2.replace("Point (", "").replace(")", "")
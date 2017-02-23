from PyQt4.QtSql import QSqlDatabase					
qgis.utils.iface.activeLayer().crs().authid()
layer = qgis.utils.iface.activeLayer()
layerName = layer.name ()
selected_features = layer.selectedFeatures()
wkt = '';
wkt = selected_features[0].geometry().exportToWkt()
print "Wkt valor "
print wkt
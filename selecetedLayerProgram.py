iface.layerTreeView().setSelectionMode( QAbstractItemView.MultiSelection )
layer=None
for lyr in QgsProject.instance().mapLayers().values():
    if lyr.name() == "LOTE_CTM":
        layer = lyr
        break

iface.layerTreeView().setCurrentLayer(layer)
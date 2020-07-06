import rhinoscriptsyntax as rs

count = rs.LayerCount()
layerNames = rs.LayerNames()
for i in range(count):
    if rs.IsLayerEmpty(layerNames[i]):
        rs.PurgeLayer(layerNames[i])
    else:
        print "The layer" + layerNames[i] + "is not empty."
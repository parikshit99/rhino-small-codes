import rhinoscriptsyntax as rs
from System.Drawing import Color
import random
#assign different materials to layers and change layer colors to correspond with it for export to lumion

def randomcolor():
    red = int(255*random.random())
    green = int(255*random.random())
    blue = int(255*random.random())
    return Color.FromArgb(red,green,blue)
    
count = rs.LayerCount()
layerNames = rs.LayerNames()
print(layerNames)
print "There are", count, "layers."
for i in range(count):
    rc = randomcolor()
    rs.LayerColor(layerNames[i], rc)
    rs.MaterialColor(i,rc)
    rs.MaterialName( i, str(i))
    rs.AddMaterialToLayer(layerNames[i])

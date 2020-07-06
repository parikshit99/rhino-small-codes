import rhinoscriptsyntax as rs

obj = rs.GetObject("Pick any object")
if obj:
    color = rs.ObjectColor(obj)
    rs.ObjectsByColor(color, True)
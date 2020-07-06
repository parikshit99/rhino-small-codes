import rhinoscriptsyntax as rs
#helps in selecting stuff exported from bim

obj = rs.GetObject("Pick any object")
if obj:
    color = rs.ObjectColor(obj)
    rs.ObjectsByColor(color, True)

# Test example for mwoffice module
# 1) Import the mwoffice module.
# 2) Create a schematic with elements and ports
# 3) Create a graph and add measurements 
# 4) Simulate

import mwoffice

office = mwoffice.CMWOffice()
office.New("MyProject")
proj = office.Project

# Create a schematic
print("\nCreate a Schematic:")
schem = proj.Schematics.Add("MySchematic")
print("Schematic Name  = {}".format(schem.Name))
print("Schematic Count = {}".format(proj.Schematics.Count))

# Add elements to the schematic (note here we depend on defaulted arguments)
print("\nAdd some elements to the schematic:")
elem1 = schem.Elements.Add("MLIN", 0, 0)
print("Element Name = {}".format(elem1.Name))

elem2 = schem.Elements.Add("MLIN", 0, 0, 180)
print("Element Name = {}".format(elem2.Name))

msub = schem.Elements.Add("MSUB", 0, 1200)
print("Element Name = {}".format(msub.Name))

# Add some ports to the schematic elements, align with nodes
print("\nAdd some ports to the schematic")
x = elem1.Nodes(2).x
y = elem1.Nodes(2).y
port1 = schem.Elements.Add("PORT", x, y, 180)
print("Port Name = {}".format(port1.Name))

x = elem2.Nodes(2).x
y = elem2.Nodes(2).y
port2 = schem.Elements.Add("PORT", x, y)
print("Port Name = {}".format(port2.Name))


# Add a graph to the project
print("Graph Count = {}".format(proj.Graphs.Count))

# Add a graph 
proj.Graphs.Add("MyGraph", mwoffice.mwGraphType.mwGT_Rectangular)

# Use default call method, doesn't require Item()
print("\nUse default method on collection to get element:")
elem = schem.Elements(1)
print("Element Name = {}".format(elem.Name))

# Access element by name
print("\nAccess element by name in a collection to get element:")
elem2 = schem.Elements(elem.Name)
print("Element Name = {}".format(elem2.Name))

# Get help on the name property of the element.
print("\nGetHelp on a class property:")
help(mwoffice.CElement.Name)

# Access some properties.
print("\nAccess some properties:")
print("Element Name = {}".format(elem.Name))
print("Element Symbol = {}".format(elem.Symbol))
print("Element RotationAngle = {}".format(elem.RotationAngle))
print("Element Flipped = {}".format(elem.Flipped))
print("Element Enabled = {}".format(elem.Enabled))

# Enumeration support for collections. This uses __iter__ and __next__
print("\nIterate schematics and their elements:")
schems = proj.Schematics
for sch in schems:
    print(sch.Name)
    elems = sch.Elements
    print("Elements = " , elems.Count)
    for el in elems:
        print(el.Name)

# Add Square Polygon to the layout.
print("\nAdd a square polygon to the layout")
lay = schem.Layout
poly = [0, 0, 0, 100e-6, 100e-6, 100e-6, 100e-6, 0]
drawingObj = lay.DrawingObjects.AddPolygon(poly, "Thick Metal")
print("Base Position = ( x = {}, y = {} )".format(drawingObj.BasePosition.x * 1e6, drawingObj.BasePosition.y * 1e6))

schem = proj.Schematics[0]
print("Indexed by name: {}".format(schem.Name))

print("Print class directly")
print(schem)
print(schems)

schem = proj.Schematics[-1]
print("Indexed by negative: {}".format(schem.Name))


for sch in schems[0:1]:
    print("indexed by range: {}".format(schem.Name))

print("Testing __dict__ output:")
print(schem.__dict__)
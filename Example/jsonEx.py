from Handler.IOPorters.jsonIn import JsonIn as VarImporter
import json

myImporter = VarImporter(Component='Fuselage',
                         VariableName='fuselage',
                         Default=35.35,
                         filePath='C:\Users\Jacopo\Desktop\Academic\GitHub\KBE_Retake\Input\Files\A3XX.json')

value = VarImporter.finder(myImporter)

Performance = {  "Performance":
  {
    "Mach cruise": {"value": 0.77, "unit": ""},
    "Wing Loading": 5000.0,
    "MTOW": 422713.0,
    "Cruise Altitude": 10000.0}
}

Configuration = {   "Configuration":
  {
    "Tail Type": "T tail",
    "Engine Position": "wing",
    "Wing Position": "low wing"
  }
}

fileJ = {}

fileJ.update(Performance)
fileJ.update(Configuration)

fout = open('C:\Users\Jacopo\Desktop\Academic\GitHub\KBE_Retake\Output\jsonfile.json', 'w')



lst1 = {}
inputs = {
    "Fuselage":
        {
            "Fuselage Length": {"value": 30.0, "unit": "m"},
            "Fuselage Diameter": {"value": 35.0, "unit": "m"},
            "Nose Slenderness": {"value": 24, "unit": ""},
            "Tail Slenderness": {"value": True, "unit": ""},
            "Tail Up Angle": {"value": 'tail up', "unit": ""}
        }
}
lst1.update(inputs)

lst2 = {}
inputs = {
    "Landing Gear":
        {
            "Landing gear height": {"value": 3.0, "unit": "m"},
            "Main Gear position": {"value": 0.8, "unit": ""},
            "Nose Gear position": {"value": 0.08, "unit": ""},
            "Lateral gear position": {"value": 0.6, "unit": ""},
            "Main wheel radius": {"value": 1.3, "unit": "m"},
            "Nose wheel radius": {"value": 0.5, "unit": "m"}
        }
}
lst2.update(inputs)

lstA = {}
lstA.update(lst1)
lstA.update(lst2)

print json.dumps(lstA,indent=4, sort_keys=True)
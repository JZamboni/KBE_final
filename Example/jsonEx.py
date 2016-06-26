from Handler.IOPorters.jsonIn import JsonIn as VarImporter
import json

fileJ = {
     "Engine": {
          "Air density at sea level": {
               "unit": "kg/m^3",
               "value": 1.225
          },
          "Cowling position": {
               "unit": "",
               "value": 0.75
          },
          "Cowling type": {
               "unit": "",
               "value": "partial"
          },
          "Engine bypass ratio": {
               "unit": "",
               "value": 3.0
          },
          "Engine-LE stagger": {
               "unit": "",
               "value": -0.15
          },
          "Mechanical efficiency": {
               "unit": "",
               "value": 0.75
          },
          "Nozzle efficiency": {
               "unit": "",
               "value": 0.97
          },
          "Speed of sound at sea level": {
               "unit": "m/s",
               "value": 340.3
          },
          "Temperature at Inlet of Turbine": {
               "unit": "K",
               "value": 1375.0
          }
     },
     "Evaluations": {
          "Htp airfoil efficiency factor": {
               "unit": "",
               "value": 0.95
          },
          "Wing airfoil efficiency factor": {
               "unit": "",
               "value": 0.95
          }
     },
     "Fuselage": {
          "Fuselage Diameter": {
               "unit": "m",
               "value": 4.0
          },
          "Fuselage Length": {
               "unit": "m",
               "value": 30.0
          },
          "Nose Slenderness": {
               "unit": "",
               "value": 1.2842911063593538
          },
          "Tail Slenderness": {
               "unit": "",
               "value": 2.11
          },
          "Tail Up Angle": {
               "unit": "",
               "value": 5.0
          }
     },
     "Htp": {
          "Horizontal height of htp in percentage of vtp": {
               "unit": "",
               "value": 1.0
          },
          "Horizontal tail Mean Aerodynamic Chord": {
               "unit": "m",
               "value": 2.2235804288336745
          },
          "Horizontal tail arm": {
               "unit": "m",
               "value": 19.32700522578115
          },
          "Horizontal tail reference surface": {
               "unit": "m^2",
               "value": 21.951346387397642
          },
          "Horizontal tail root chord": {
               "unit": "m",
               "value": 2.9932813465068695
          },
          "Horizontal tail span": {
               "unit": "m",
               "value": 10.476484712774043
          },
          "Horizontal tail tip chord": {
               "unit": "m",
               "value": 1.1973125386027479
          },
          "Horizontal tail volume coefficient": {
               "unit": "",
               "value": 1.4421606276380152
          },
          "Htp aspect ratio": {
               "unit": "",
               "value": 5.0
          },
          "Htp sweep at quarter chord": {
               "unit": "deg",
               "value": 38.7695601900826
          },
          "Htp taper ratio": {
               "unit": "",
               "value": 0.4
          },
          "Span percentage for xFoil analysis": {
               "unit": "",
               "value": 0.5
          }
     },
     "Landing Gear": {
          "Landing gear height": {
               "unit": "m",
               "value": 1.6
          },
          "Lateral gear position": {
               "unit": "",
               "value": 1.8
          },
          "Main Gear position": {
               "unit": "",
               "value": 0.6
          },
          "Main wheel radius": {
               "unit": "m",
               "value": 0.5
          },
          "Nose Gear position": {
               "unit": "",
               "value": 0.08
          },
          "Nose wheel radius": {
               "unit": "m",
               "value": 0.3
          }
     }
}

for component in fileJ:
    print component
    for variable in fileJ[component]:
        print "      " + variable
        value = fileJ[component][variable]["value"]
        print "              " + repr(value)
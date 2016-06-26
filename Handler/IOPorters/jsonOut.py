import json
import os

class JsonOut:

    def __init__(self,ListValues, outputPath):
        self.path = outputPath
        self.listValues = ListValues




    def writer(self):

        print json.dumps(self.listValues, indent=5, sort_keys=True)
        fout = open(self.path, 'w')
        json.dump(self.listValues, fout, indent=5, sort_keys=True)
        return "Output file correctly generated"
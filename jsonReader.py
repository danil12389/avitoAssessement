import json
import glob

class JsonReader():

    def openAndTransformJson(self):
        f = open(glob.glob('*.json')[0])
        result = json.load(f)
        f.close()
        return result

    def getNumberOfChannels(self):
        jsonBody = self.openAndTransformJson()
        return len(jsonBody['channels'])
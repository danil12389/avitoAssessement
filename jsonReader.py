import json
import glob

class JsonReader():

    def openAndTransformJson(self, filePath):

        if (filePath == -1):
            f = open(glob.glob('*.json')[0])
            result = json.load(f)
            f.close()
        else:
            f = open(filePath)
            result = json.load(f)
            f.close()
        return result

    def getNumberOfChannels(self, filePath):
        jsonBody = self.openAndTransformJson(filePath)
        return len(jsonBody['channels'])
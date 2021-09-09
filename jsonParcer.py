from jsonReader import *

class JsonParcer():

    def parseChannels(self, transformedJson, size):
        listOfChannels = []
        for i in range(size):
            listOfChannels.append(transformedJson['channels'][i]['channel'])
        return listOfChannels

    def parseMessages(self, transformedJson, size):
        listOfMessages = []
        for i in range(size):
            listOfMessages.append(transformedJson['channels'][i]['text'])
        return listOfMessages       
   
    def getToken(self, transformedJson):
        return transformedJson['bot_token']    
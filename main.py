from jsonReader import *
from jsonParcer import *
import slack
import sys

def main():

    jsonReaded  = JsonReader()
    jsonTransformed = JsonParcer()

    if (len(sys.argv) == 1):
        pathToFile = -1
    else:
        pathToFile = sys.argv[1]

    
    client = slack.WebClient(token = jsonTransformed.getToken(jsonReaded.openAndTransformJson(pathToFile)))
    channels = jsonTransformed.parseChannels(jsonReaded.openAndTransformJson(pathToFile), jsonReaded.getNumberOfChannels(pathToFile))
    messages = jsonTransformed.parseMessages(jsonReaded.openAndTransformJson(pathToFile), jsonReaded.getNumberOfChannels(pathToFile))
    for i in range(jsonReaded.getNumberOfChannels(pathToFile)):
        client.chat_postMessage(channel= '#'+ channels[i], text = messages[i])

   
main()
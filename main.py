from jsonReader import *
from jsonParcer import *
import slack

def main():

    jsonReaded  = JsonReader()
    jsonTransformed = JsonParcer()
    client = slack.WebClient(token = jsonTransformed.getToken(jsonReaded.openAndTransformJson()))
    channels = jsonTransformed.parseChannels(jsonReaded.openAndTransformJson(), jsonReaded.getNumberOfChannels())
    messages = jsonTransformed.parseMessages(jsonReaded.openAndTransformJson(), jsonReaded.getNumberOfChannels())
    for i in range(jsonReaded.getNumberOfChannels()):
        client.chat_postMessage(channel= '#'+ channels[i], text = messages[i])


main()
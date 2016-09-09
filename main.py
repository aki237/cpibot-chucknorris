from bot import bot
import json
import urllib

def botlogic (M) :
    if M.Channel is not "broadcast" :
        url = "http://api.icndb.com/jokes/random"
        resp = urllib.urlopen(url).read()
        result = json.loads(resp)
        if result["type"] == "success" :
            return  result["value"]["joke"], True
        return "Unable to reach the database", True

bot = bot.Bot("pybot","192.168.0.100",6672,botlogic)
bot.Run()

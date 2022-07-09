import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "") # Make a bot from https://t.me/BotFather and enter the token here
    
    APP_ID = int(os.environ.get("API_ID", 12345)) # Get this value from https://my.telegram.org/apps
    
    API_HASH = os.environ.get("API_HASH", "") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(os.environ.get("OWNER_ID", None)) # Your(owner's) telegram id
    
    MONGO_STR = os.environ.get("MONGO_STR", "mongodb+srv://erichdaniken:erichdaniken@cluster0.c13qk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") # Get from MongoDB Atlas

    DOWNLOAD_LOCATION = "app//DOWNLOADS//" # The download location for users. (Don't change anything in this field!)

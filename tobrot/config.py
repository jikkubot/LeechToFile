import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1288713654:AAHaJ7G2S0w3hmPrraKYBfTJexWJC47MXVs")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 1618055))
    API_HASH = os.environ.get("API_HASH", "a4a50a6e5f9b8550884d61d7ee49e5f4")
    OWNER_ID = int(os.environ.get("OWNER_ID", 976661372))
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = set(int(x) for x in os.environ.get("AUTH_CHANNEL", "-1001161510664").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", 6800))
    EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", 15))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(os.environ.get("MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START", 600))
    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 1072864000))
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "█")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "░")
    # add offensive API
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    CUSTOM_FILE_NAME = os.environ.get("CUSTOM_FILE_NAME", "")
    LEECH_COMMAND = os.environ.get("LEECH_COMMAND", "leech@JikkutorfileBot")
    YTDL_COMMAND = os.environ.get("YTDL_COMMAND", "ytdl@JikkutorfileBot")
    PYTDL_COMMAND = os.environ.get("PYTDL_COMMAND", "pytdl")
    RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", "")
    DESTINATION_FOLDER = os.environ.get("DESTINATION_FOLDER", "TorrentLeech-Gdrive")
    INDEX_LINK = os.environ.get("INDEX_LINK", "")
    CANCEL_COMMAND_G = os.environ.get("CANCEL_COMMAND_G", "cancel")
    GET_SIZE_G = os.environ.get("GET_SIZE_G", "getsize")
    STATUS_COMMAND = os.environ.get("STATUS_COMMAND", "status")
    SAVE_THUMBNAIL = os.environ.get("SAVE_THUMBNAIL", "savethumbnail@JikkutorfileBot")
    CLEAR_THUMBNAIL = os.environ.get("CLEAR_THUMBNAIL", "clearthumbnail@JikkutorfileBot")
    CLEAR_UNDELETED = os.environ.get("CLEAR_UNDELETED", "clearall")
    LOG_COMMAND = os.environ.get("LOG_COMMAND", "getlog") 

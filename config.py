import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "22878164"))
API_HASH = getenv("API_HASH", "b02f3f16d2e97d11dedaa68624fa5edf")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7227577890:AAEJHYLMGJejskg8cwCIo4bCxYAF5MHueow")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://erkbwrs084:909090@cluster0.qdrfgmb.mongodb.net/?retryWrites=true&w=majority")


DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 960))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002238574089"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7305205222"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", #ticaret
    "https://t.me/ikidebirsakinleri", 
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/pulseduyuru") #duyuru
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Sohbetikidebir") #gurup

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", None)

# Time after which you're assistant account will leave chats automatically.

AUTO_LEAVE_ASSISTANT_TIME = int(

    getenv("ASSISTANT_LEAVE_TIME", "999999999999")

)  # Remember to give value in Seconds

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2041df9cbcd142cba804578a2cf85939")

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "80ffd296320e49299830e80b11e3bf73")

# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BAFdF9QAQi4Xv4ghG96zb3P4RKu2cne2pUeuIoXm4S0u-3AFwtbj8THuVj0-g69c66k1dh8gBF9ADSvr_uyVqczMHjBBiqP1ezwBNplInQLfZaQk04T9NIbgxkPChjE5PSySRTdSi4U_Yz7Pn6z1sSmZThP0fYrjOMXOaAdRlnB7Gtak06bw8LzmWatxmCpnOd20NdRZVtACD2LUkE-ArQ3F-fhqw1AA5NlXpbQjsVlWFo4tKhbD4zx8Gr2mQ_0-O6Lao1QS0mHNsESrUAmhM0HDZo7atSmZffO1cjLEb7geezqYMZG_VAcY6lB0Cemahjl7EkVRuhcQy-IMdLpOhvOG2K-0dAAAAAF-0u0JAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
)
PLAYLIST_IMG_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
STATS_IMG_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
TELEGRAM_AUDIO_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
TELEGRAM_VIDEO_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
STREAM_IMG_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
SOUNCLOUD_IMG_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
YOUTUBE_IMG_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
SPOTIFY_ARTIST_IMG_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
SPOTIFY_ALBUM_IMG_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
SPOTIFY_PLAYLIST_IMG_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))



if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

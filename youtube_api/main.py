import os
from youtube_statistics import YouTubeStatistics
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("GCP_DEVELOPMENT_API_KEY")
BRILLIANT_IDIOTS_CHANNEL_ID = "UC9pQOZJsjiX7UMc_UZFjpLg"
TUMIE_NT_CHANNEL_ID = "UC8VyxyMUJHPOg0I0JfO7AwQ"
ZIBO_BANTSI_CHANNEL_ID = "UCG-mU5uWB6sRdHh9Aa84t9Q"


yt = YouTubeStatistics(API_KEY, ZIBO_BANTSI_CHANNEL_ID)
yt.get_channel_statistics()
yt.get_channel_video_info()
yt.dump_to_json_file()


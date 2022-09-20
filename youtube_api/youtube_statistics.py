import requests
import json
from tqdm import tqdm


class YouTubeStatistics:

    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_title = ""
        self.channel_statistics = None
        self.video_data = None

    def get_channel_statistics(self):
        url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={self.channel_id}&key={self.api_key}"
        json_url = requests.get(url)
        data = json.loads(json_url.text)

        try:
            channel_title = data["items"][0]["snippet"]["title"]
            data = data["items"][0]["statistics"]
        except:
            data = None

        self.channel_title = channel_title
        self.channel_statistics = data
        return self.channel_statistics

    def get_channel_video_info(self):
        channel_videos = self._get_channel_videos(10)
        video_info = ["snippet", "contentDetails", "statistics"]
        for video_id in tqdm(channel_videos):
            for info in video_info:
                data = self._get_video_data(video_id, info)
                channel_videos[video_id].update(data)
        self.video_data = channel_videos
        return self.video_data

    def _get_video_data(self, video_id, info):
        url = f"https://youtube.googleapis.com/youtube/v3/videos?key={self.api_key}&id={video_id}&part={info}"
        response = requests.get(url)
        data = json.loads(response.text)
        try:
            data = data["items"][0][info]
        except:
            print(f"failed to get video info on video_id: {video_id}, info: {info}")
            data = dict()
        return data

    def _get_channel_videos(self, limit=None):
        """A helper function to get all videos for the channel, the limit is to specify the number of
        videos you want fetched."""
        url = f"https://youtube.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.channel_id}&" \
                    f"part=id&order=date"
        if limit is not None and isinstance(limit, int):
            url += "&maxResults=" + str(limit)

        videos, next_page_token = self._get_channel_videos_per_page(url)
        mimimum_number_of_api_calls = 0
        while next_page_token is not None and mimimum_number_of_api_calls < 10:
            next_url = url + "&pageToken=" + next_page_token
            next_videos, next_page_token = self._get_channel_videos_per_page(next_url)
            videos.update(next_videos)
            mimimum_number_of_api_calls += 1
        return videos

    def _get_channel_videos_per_page(self, url):
        fetch_url = requests.get(url)
        data = json.loads(fetch_url.text)
        channel_videos = dict()

        if "items" not in data:
            return channel_videos,None

        response_items = data["items"]
        next_page_token = data.get("nextPageToken", None)

        for item in response_items:
            try:
                kind = item["id"]["kind"]
                if kind == "youtube#video":
                    video_id = item["id"]["videoId"]
                    channel_videos[video_id] = dict()
            except KeyError:
                print("Could not get channel videos per page")
        return channel_videos, next_page_token


    def dump_to_json_file(self):
        """Get the statistics of the api call and dump them to a json file"""
        if self.channel_statistics is None or self.video_data is None:
            print("empty")
            return

        channel_information = { self.channel_id: { "channel_statistics": self.channel_statistics, "channel_video_data": self.video_data } }

        channel_title = self.channel_title
        channel_title = channel_title.replace(" ", "_").lower() #replace spaces with underscores
        with open(self._create_json_file_name(channel_title), "w") as json_file:
            json.dump(channel_information, json_file, indent=4)
        print("file dumped")

    def _create_json_file_name(self,channel_title):
        """Generate a file and add an extension."""
        return channel_title + ".json"

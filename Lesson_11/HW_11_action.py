import datetime
from abc import ABC, abstractmethod
from typing import List


class SocialChannel(ABC):
    def __init__(self, type: str, followers: int):
        self.type = type
        self.followers = followers

    @abstractmethod
    def post_message(self, message: str):
        pass

    @abstractmethod
    def process_schedule(self, posts: List["Post"]):
        pass


class Post:
    def __init__(self, message: str, timestamp: int):
        self.message = message
        self.timestamp = timestamp


class YoutubeChannel(SocialChannel):
    def post_message(self, message: str) -> None:
        print(f"Post on YouTube: {message}")

    def process_schedule(posts: List[Post]) -> None:
        current_time = datetime.datetime.now()
        for post in posts:
            if post.timestamp <= current_time:
                self.post_message(post.message)  # noqa


class FacebookChannel(SocialChannel):
    def post_message(self, message: str) -> None:
        print(f"Post on Facebook: {message}")

    def process_schedule(posts: List[Post]) -> None:
        current_time = datetime.datetime.now()
        for post in posts:
            if post.timestamp <= current_time:
                self.post_message(post.message)  # noqa


class TwitterChannel(SocialChannel):
    def post_message(self, message: str) -> None:
        print(f"Post on Twitter: {message}")

    def process_schedule(posts: List[Post]) -> None:
        current_time = datetime.datetime.now()
        for post in posts:
            if post.timestamp <= current_time:
                self.post_message(post.message)  # noqa


def dispatcher(channel_type: str, followers: int) -> SocialChannel:
    if channel_type == "youtube":
        return YoutubeChannel(type="youtube", followers=followers)
    elif channel_type == "facebook":
        return FacebookChannel(type="facebook", followers=followers)
    elif channel_type == "twitter":
        return TwitterChannel(type="twitter", followers=followers)


youtube_channel = YoutubeChannel("youtube", 1000000)
facebook_channel = FacebookChannel("facebook", 500000)
twitter_channel = TwitterChannel("twitter", 200000)


channels = [youtube_channel, facebook_channel, twitter_channel]

posts = [
    Post("Hello YouTube!", 10.20),
    Post("Hello Facebook!", 11.00),
    Post("Hello Twitter", 7.25),
]

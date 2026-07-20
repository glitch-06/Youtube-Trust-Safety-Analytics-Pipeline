from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY
import pandas as pd

youtube = build(
    "youtube",
    "v3",
    developerKey=YOUTUBE_API_KEY
)


def search_videos(query, max_results=10):

    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=max_results
    )

    response = request.execute()

    videos = []

    for item in response["items"]:

        # Skip results without a videoId
        if "videoId" not in item["id"]:
            continue

        videos.append({
            "keyword": query,
            "title": item["snippet"]["title"],
            "video_id": item["id"]["videoId"],
            "channel": item["snippet"]["channelTitle"]
        })

    return videos


if __name__ == "__main__":

    keywords = [
        "MrBeast",
        "PewDiePie",
        "Linus Tech Tips",
        "Bitcoin",
        "Ethereum",
        "Crypto Scam",
        "AI",
        "OpenAI",
        "Google",
        "YouTube",
        "Taylor Swift",
        "Gaming",
        "Football",
        "News",
        "Music"
    ]

    all_videos = []

    for keyword in keywords:
        print(f"Searching: {keyword}")
        all_videos.extend(search_videos(keyword))

    df = pd.DataFrame(all_videos)

    df.to_csv("data/videos.csv", index=False)

    print(f"\nSaved {len(df)} videos to data/videos.csv")
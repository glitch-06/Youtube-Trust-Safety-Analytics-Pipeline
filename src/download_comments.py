from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY
import pandas as pd
import time

youtube = build(
    "youtube",
    "v3",
    developerKey=YOUTUBE_API_KEY
)


def get_comments(video_id, limit=100):

    comments = []

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText"
    )

    while request and len(comments) < limit:

        response = request.execute()

        for item in response["items"]:

            snippet = item["snippet"]["topLevelComment"]["snippet"]

            comments.append({

                "comment_id": item["snippet"]["topLevelComment"]["id"],

                "video_id": video_id,

                "author_name": snippet["authorDisplayName"],

                "author_channel_id":
                snippet.get("authorChannelId", {}).get("value"),

                "comment_text": snippet["textDisplay"],

                "like_count": snippet["likeCount"],

                "published_at": snippet["publishedAt"],

                "updated_at": snippet["updatedAt"]

            })

            if len(comments) >= limit:
                break

        request = youtube.commentThreads().list_next(request, response)

    return comments


videos = pd.read_csv("data/videos.csv")

START = 0
END = 10

videos = videos.iloc[START:END]

all_comments = []

for index, row in videos.iterrows():

    print(f"{index+1}/{len(videos)}  {row['title']}")

    try:

        comments = get_comments(row["video_id"], limit=50)

        all_comments.extend(comments)

        print(f"Collected {len(comments)} comments")

    except Exception as e:

        print("Skipped:", e)

    time.sleep(0.2)

df = pd.DataFrame(all_comments)

df.to_csv("data/all_comments.csv", index=False)

print("\n===================================")
print(f"Total Comments: {len(df)}")
print("Saved to data/all_comments.csv")
print("===================================")
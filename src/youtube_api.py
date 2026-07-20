from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY
import pandas as pd

youtube = build(
    "youtube",
    "v3",
    developerKey=YOUTUBE_API_KEY
)


def get_video_comments(video_id, max_results=100):
    comments = []

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=min(max_results, 100),
        textFormat="plainText"
    )

    while request:
        response = request.execute()

        for item in response["items"]:
            snippet = item["snippet"]["topLevelComment"]["snippet"]

            comments.append({
                "comment_id": item["snippet"]["topLevelComment"]["id"],
                "video_id": video_id,
                "author_name": snippet["authorDisplayName"],
                "author_channel_id": snippet.get("authorChannelId", {}).get("value"),
                "comment_text": snippet["textDisplay"],
                "like_count": snippet["likeCount"],
                "published_at": snippet["publishedAt"],
                "updated_at": snippet["updatedAt"]
            })

            if len(comments) >= max_results:
                return comments

        request = youtube.commentThreads().list_next(request, response)

    return comments


if __name__ == "__main__":

    video_id = "dQw4w9WgXcQ"

    comments = get_video_comments(video_id, max_results=200)

    df = pd.DataFrame(comments)

    df.to_csv("data/comments.csv", index=False)

    print(f"Downloaded {len(df)} comments.")
    print("Saved to data/comments.csv")
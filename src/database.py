import pandas as pd
import psycopg2
from config import DB_CONFIG


def get_connection():
    return psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )


def insert_comments(csv_file):

    df = pd.read_csv(csv_file)

    conn = get_connection()
    cur = conn.cursor()

    inserted = 0

    for _, row in df.iterrows():

        try:

            cur.execute("""
            INSERT INTO comments
            (
                comment_id,
                video_id,
                author_name,
                author_channel_id,
                comment_text,
                like_count,
                published_at,
                updated_at
            )

            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)

            ON CONFLICT (comment_id)
            DO NOTHING;
            """,

            (
                row["comment_id"],
                row["video_id"],
                row["author_name"],
                row["author_channel_id"],
                row["comment_text"],
                int(row["like_count"]),
                row["published_at"],
                row["updated_at"]
            )
            )

            inserted += 1

        except Exception as e:
            print(e)

    conn.commit()

    print(f"{inserted} comments inserted.")

    cur.close()
    conn.close()


if __name__ == "__main__":

    insert_comments("data/comments.csv")
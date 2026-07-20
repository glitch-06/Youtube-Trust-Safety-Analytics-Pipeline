import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from pathlib import Path

from config import DB_CONFIG

password = quote_plus(DB_CONFIG["password"])

engine = create_engine(
    f"postgresql+psycopg2://{DB_CONFIG['user']}:{password}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

folder = Path("data/raw")

csv_files = sorted(folder.glob("*.csv"))

for file in csv_files:

    print(f"Loading {file.name}...")

    df = pd.read_csv(file)

    df.columns = [
        "comment_id",
        "author",
        "date",
        "content",
        "video_name",
        "class"
    ]

    df.to_sql(
        "youtube_comments",
        engine,
        if_exists="append",
        index=False
    )

    print(f"Imported {len(df)} rows")

print("All files imported successfully!")
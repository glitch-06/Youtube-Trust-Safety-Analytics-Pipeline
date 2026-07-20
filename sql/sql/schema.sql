DROP TABLE IF EXISTS youtube_comments;

CREATE TABLE youtube_comments (
    comment_id VARCHAR(100),
    author VARCHAR(255),
    date TIMESTAMP,
    content TEXT,
    class INT
);
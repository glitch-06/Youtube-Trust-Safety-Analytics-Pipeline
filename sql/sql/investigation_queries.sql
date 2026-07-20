-- Duplicate Comment IDs
SELECT
    comment_id,
    COUNT(*) AS occurrences
FROM youtube_comments
GROUP BY comment_id
HAVING COUNT(*) > 1
ORDER BY occurrences DESC;

--Duplicate Comment IDs

SELECT
    content,
    COUNT(*) AS occurrences
FROM youtube_comments
GROUP BY content
HAVING COUNT(*) > 1
ORDER BY occurrences DESC;

--Same Author Posting the Same Comment

SELECT
    author,
    content,
    COUNT(*) AS occurrences
FROM youtube_comments
GROUP BY author, content
HAVING COUNT(*) > 1
ORDER BY occurrences DESC;


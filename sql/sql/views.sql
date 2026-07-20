CREATE OR REPLACE VIEW high_risk_authors AS
SELECT
    author,
    COUNT(*) AS total_comments,
    SUM(CASE WHEN class = 1 THEN 1 ELSE 0 END) AS spam_comments,
    ROUND(
        100.0 * SUM(CASE WHEN class = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS spam_rate
FROM youtube_comments
GROUP BY author
HAVING COUNT(*) >= 3;
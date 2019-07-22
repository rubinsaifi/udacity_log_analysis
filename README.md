CREATE VIEW total_logs AS
SELECT date(time) as dt, count(*) AS total
FROM log GROUP BY date(time) ORDER BY total;

CREATE VIEW error_logs AS
SELECT date(time) as dt, count(*) AS error
FROM log WHERE status!='200 OK'
GROUP BY date(time) ORDER BY error;

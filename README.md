# Udacity's Log Analysis Project (Full Stack Web Developer Nanodegree)

## Requirements
- Python3
- Linux Machine (either VM or main)
- PostgreSQL db

## Importing DB files
Download sql zip file from [newdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) into linux vm and perform following steps:
```
$ unzip newdata.zip 
$ psql -d news -f newsdata.sql
```
Connect to news db
```
$ psql -d news
```

## DB Views

### total_logs view
```
CREATE VIEW total_logs AS SELECT 
date(time) as dt, count(*) AS total 
FROM log GROUP BY date(time) ORDER BY total;
```
### error_logs view
```
CREATE VIEW error_logs AS SELECT
date(time) as dt, count(*) AS error
FROM log WHERE status!='200 OK'
GROUP BY date(time) ORDER BY error;
```

# Running Program
```
$ python3 log_analysis.py
```

import psycopg2
import sys


def main():
    """Udacity: Log Analysis"""

    conn = psycopg2.connect(database="news")
    if not conn:
        print("Unable to connect to db\nExiting...")
        sys.exit()
    cur = conn.cursor()

    # Q1. What are the most popular three articles of all time?
    popular_article = """select a.title, t.counts from articles a, \
        (select count(*) counts, substring(path from 10) as xpath \
        from log where path!='/' group by path order by counts desc limit 3) \
        as t where  a.slug=t.xpath order by t.counts desc;"""

    cur.execute(popular_article)
    resp = cur.fetchall()

    print("# Answer to Q1")
    for k, v in resp:
        print ('"{}" -- {} views'.format(k, v))
    print(" ")

    """
    should print following
    # Answer to Q1
    "Candidate is jerk, alleges rival" -- 338647 views
    "Bears love berries, alleges bear" -- 253801 views
    "Bad things gone, say good people" -- 170098 views
    """
    # end-of-q1

    # Q2. Who are the most popular article authors of all time?
    popular_authors = """select authors.name, sum(tmp.total) as sums from \
        authors, (select articles.author as author , tpx.view as total from \
        articles join (select count(*) as view, substring(path from 10) as \
        xpath from log where path like '/article/%' group by xpath order by \
        view desc) as tpx on tpx.xpath = articles.slug) as tmp where \
        authors.id = tmp.author group by authors.name order by sums desc"""

    cur.execute(popular_authors)
    resp = cur.fetchall()

    print("# Answer to Q2")
    for k, v in resp:
        print ('{} -- {} views'.format(k, v))
    print(" ")

    """
    should print following
    # Answer to Q2
    Ursula La Multa -- 507594 views
    Rudolf von Treppenwitz -- 423457 views
    Anonymous Contributor -- 170098 views
    Markoff Chaney -- 84557 views
    """
    # end-of-q2

    # Q3. On which days did more than 1% of requests lead to errors?
    error_date = """select error_logs.dt, (100.0*error/total) as percent FROM \
        error_logs, total_logs WHERE error_logs.dt = total_logs.dt ORDER BY \
        percent desc"""

    cur.execute(error_date)
    resp = cur.fetchone()

    print("# Answer to Q2")
    print("{} -- {}% errors".format(resp[0], round(resp[1], 2)))

    """
    should print following
    # Answer to Q2
    2016-07-17 -- 2.26% errors
    """
    # end-of-q3


if __name__ == '__main__':
    main()

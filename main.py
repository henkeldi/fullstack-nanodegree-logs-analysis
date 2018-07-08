#!/usr/bin/python2
# -*- coding: utf-8 -*-
import psycopg2

DBNAME = "news"
ERROR_THRESHOLD = 0.01


def main():
    '''Performs a series of database queries to analyze the
        log data and print out the answers to some qustions'''
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()

    # This query finds the most popular three articles of all time
    query = '''SELECT articles.title, count(*) as n
                FROM articles, log
                WHERE ('/article/' || articles.slug) = log.path
                    AND log.method = 'GET'
                    AND log.status = '200 OK'
                GROUP BY articles.title
                ORDER BY n DESC
                LIMIT 3'''
    c.execute(query)
    results = c.fetchall()

    print '1. What are the most popular three articles of all time?'
    print '\n'.join(['\"{}\" — {:,} views'.format(*r) for r in results])
    print

    # This query finds the most popular article authors of all time
    query = '''SELECT authors.name, count(*) as n
                FROM authors, articles, log
                WHERE authors.id = articles.author
                    AND ('/article/' || articles.slug) = log.path
                    AND log.method = 'GET'
                    AND log.status = '200 OK'
                GROUP BY authors.name
                ORDER BY n DESC'''
    c.execute(query)
    results = c.fetchall()

    print '2. Who are the most popular article authors of all time?'
    print '\n'.join(['{} — {:,} views'.format(*r) for r in results])
    print

    # This query finds the days on which ERROR_THRESHOLD % of requests
    # led to errors
    query = '''SELECT total_sums.time, error_sum / total_sum
        FROM (SELECT log.time::date as time, count(*)::float as total_sum
                FROM log
                GROUP BY log.time::date) as total_sums,
            (SELECT log.time::date as time, count(*)::float as error_sum
                FROM log
                WHERE status = '404 NOT FOUND'
                GROUP BY log.time::date) as error_sums
        WHERE total_sums.time = error_sums.time
            AND error_sum / total_sum > {}'''.format(ERROR_THRESHOLD)
    c.execute(query)
    results = c.fetchall()

    print '3. On which days did more than {:.1%} of requests lead to errors?'\
        .format(ERROR_THRESHOLD)
    print '\n'.join(
        ['{0:%B} {0:%d}, {0:%Y} — {1:.1%} errors'.format(*r) for r in results])
    print

    db.close()


if __name__ == '__main__':
    main()

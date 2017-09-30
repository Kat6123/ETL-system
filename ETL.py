#!/usr/bin/env python
# -*- coding: utf-8 -*-


import psycopg2
import csv


def main():
    with psycopg2.connect("dbname='kat' user='kat' "
                          "host='localhost' password='3g1o4h5t'") as db:
        cur = db.cursor()
        with open("jobs.csv") as fp:
            csv_reader = csv.reader(fp)
            for row in csv_reader:
                cur.execute("""INSERT into snap_jobs."Jobs"
                            (job_title, category, status, location)
                            VALUES ('{0}', '{1}', '{2}', '{3}')""".format(
                                row[0], row[1], row[2], row[3]
                            ))
        db.commit()


if __name__ == '__main__':
    main()

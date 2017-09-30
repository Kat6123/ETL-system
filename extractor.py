#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv
import bs4

output_html = "jobs.html"
output_csv = "jobs.csv"


def main():
    title_tuple = ("Job Title", "Category", "Status", "Location")
    with open(output_html, "r") as fp:
        soup = bs4.BeautifulSoup(fp, "lxml")

    with open(output_csv, "wb") as fp:
        csv_writer = csv.writer(fp)
        csv_writer.writerow(title_tuple)

        for row in soup.find_all('tr'):
            row_to_write = tuple(
                (r.encode('utf-8') for r in row.stripped_strings)
            )
            csv_writer.writerow(row_to_write)


if __name__ == '__main__':
    main()

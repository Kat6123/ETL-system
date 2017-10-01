# -*- coding: utf-8 -*-

import pyvirtualdisplay.smartdisplay as smartdisplay
import selenium.webdriver
import contextlib
import time
import csv
import bs4
import psycopg2


BROWSER_JS_EXEC_PAUSE = 2
DEFAULT_ENCODING = 'utf-8'
CSV_HEADER = ('Job Title', 'Category', 'Status', 'Location')
HTML_ROW_TAG = 'tr'


def download_html(site_url, output_file):
    with smartdisplay.SmartDisplay(visible=0, bgcolor='black'):
        with contextlib.closing(selenium.webdriver.Chrome()) as browser:
            browser.get(site_url)

            time.sleep(BROWSER_JS_EXEC_PAUSE)

            browser.execute_script("window.scrollTo "
                                   "(0, document.body.scrollHeight);")

            with open(output_file, "w") as fp:
                fp.write(browser.page_source.encode(DEFAULT_ENCODING))


def extract_into_csv(input_html, output_csv):
    with open(input_html, "r") as fp:
        soup = bs4.BeautifulSoup(fp, "lxml")

    with open(output_csv, "w") as fp:
        csv_writer = csv.writer(fp)

        csv_writer.writerow(CSV_HEADER)

        for row in soup.find_all(HTML_ROW_TAG):
            row_to_write = tuple(
                (r.encode(DEFAULT_ENCODING) for r in row.stripped_strings)
            )
            csv_writer.writerow(row_to_write)


def download_to_bd(input_csv):
    with psycopg2.connect("dbname='kat' user='kat' "
                          "host='localhost' password='3g1o4h5t'") as db:
        cur = db.cursor()
        with open(input_csv) as fp:
            csv_reader = csv.reader(fp)
            for row in csv_reader:
                cur.execute("""INSERT into snap_jobs."Jobs"
                            (job_title, category, status, location)
                            VALUES ('{0}', '{1}', '{2}', '{3}')""".format(
                                row[0], row[1], row[2], row[3]
                            ))
        db.commit()

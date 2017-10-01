# -*- coding: utf-8 -*-

import pyvirtualdisplay.smartdisplay as smartdisplay
import selenium.webdriver
import contextlib
import time
import csv
import bs4
import psycopg2

import settings


def download_html(site_url, output_file):
    with smartdisplay.SmartDisplay(visible=0, bgcolor='black'):
        with contextlib.closing(selenium.webdriver.Chrome()) as browser:
            browser.get(site_url)

            time.sleep(settings.BROWSER_JS_EXEC_PAUSE)

            browser.execute_script("window.scrollTo "
                                   "(0, document.body.scrollHeight);")

            with open(output_file, "w") as fp:
                fp.write(browser.page_source.encode(settings.DEFAULT_ENCODING))


def extract_into_csv(input_html, output_csv):
    with open(input_html, "r") as fp:
        soup = bs4.BeautifulSoup(fp, "lxml")

    with open(output_csv, "w") as fp:
        csv_writer = csv.writer(fp)

        csv_writer.writerow(settings.CSV_HEADER)

        for row in soup.find_all('tr'):
            row_to_write = tuple(
                (r.encode(settings.DEFAULT_ENCODING)
                    for r in row.stripped_strings)
            )
            csv_writer.writerow(row_to_write)


def download_to_bd(input_csv):
    try:
        with psycopg2.connect(**(settings.DATABASE_SETTINGS)) as db:
            cur = db.cursor()

            query = """INSERT into snap_jobs."Jobs"
                    (job_title, category, status, location)
                    VALUES ('{}', '{}', '{}', '{}')"""

            with open(input_csv) as fp:
                csv_reader = csv.reader(fp)

                csv_reader.next()

                for row in csv_reader:
                    cur.execute(query.format(*row))

            db.commit()

    except psycopg2.IntegrityError as error:
        print(error)

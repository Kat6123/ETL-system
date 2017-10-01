#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

from etl_functionality import (
    download_html,
    download_to_bd,
    extract_into_csv
)

SITE_URL = "https://www.snap.com/en-US/jobs/"
HTML_FILE = "snap.html"
CSV_FILE = "snap.csv"


def main():
    download_html(SITE_URL, HTML_FILE)
    extract_into_csv(HTML_FILE, CSV_FILE)
    download_to_bd(CSV_FILE)


if __name__ == '__main__':
    main()

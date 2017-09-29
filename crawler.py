#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pyvirtualdisplay.smartdisplay as smartdisplay
import selenium.webdriver
import contextlib
import BeautifulSoup
import time

BROWSER_DOWNLOAD_PAUSE = 2
site_address = "https://www.snap.com/en-US/jobs/"
output_html = "jobs.html"


def main():
    # _, site_address, output_html = sys.argv

    with smartdisplay.SmartDisplay(visible=0, bgcolor='black') as disp:
        with contextlib.closing(selenium.webdriver.Chrome()) as driver:
            driver.get(site_address)

            time.sleep(BROWSER_DOWNLOAD_PAUSE)

            driver.execute_script("window.scrollTo"
                                  "(0, document.body.scrollHeight);")
            soup = BeautifulSoup.BeautifulSoup(driver.page_source)
            with open(output_html, "w") as fp:
                fp.write(soup.prettify())


if __name__ == '__main__':
    main()

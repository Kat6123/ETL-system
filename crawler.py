#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pyvirtualdisplay.smartdisplay as smartdisplay
import selenium.webdriver
import contextlib
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

            with open(output_html, "w") as fp:
                fp.write(driver.page_source.encode('utf-8'))


if __name__ == '__main__':
    main()

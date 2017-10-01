#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

from etl_functionality import download_html


def main():
    _, site_address, output_html = sys.argv

    download_html(site_address, output_html)


if __name__ == '__main__':
    main()

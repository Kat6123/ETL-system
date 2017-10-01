#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from etl_functionality import extract_into_csv


def main():
    _, input_html, output_csv = sys.argv

    extract_into_csv(input_html, output_csv)


if __name__ == '__main__':
    main()

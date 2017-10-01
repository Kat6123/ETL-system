#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

from etl_functionality import download_to_bd


def main():
    _, input_csv = sys.argv

    download_to_bd(input_csv)


if __name__ == '__main__':
    main()

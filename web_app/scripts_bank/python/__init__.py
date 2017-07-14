#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Copyright (c) 2017 Gabor, Kis-Hegedus
# All Rights Reserved.
#
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""Project

Project Description

"""

""" Imports """
import argparse
import logging as log

"""Functions & Methods"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("excel_file", help="Name and path of the Excel file")
    parser.add_argument("-s", "--sheet", help="Name of the sheet to get data from.", default="scripting")
    parser.add_argument("-D", "--debug", help="Enable debug mode", action="store_true")
    parser.add_argument("-L", "--list_all", help="Use all the elements from the Excel Table", action="store_true")
    parser.add_argument("-C", "--clean_up", help="Remove the content of ./Outputs/ folder.", action="store_true")
    parser.add_argument("-r", "--max_row_count", help="Provide the max row count", action="store")
    args = parser.parse_args()
    if args.debug:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.INFO)

    """ Main program """


if __name__ == '__main__':
    main()
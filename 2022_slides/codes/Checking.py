#!/usr/bin/env python3
# By Le Chen
# chenle02@gmail.com / le.chen@auburn.edu
#
# -*- coding: utf-8 -*-
"""
    codes.Checking
    ~~~~~~~~~~~~~~

    DESCRIPTION
    Use this script to check if there are matching date-of-birth (DOB) in the second column of the given CSV file.

    :copyright: (c) 2022 by Le Chen (chenle02@gamil.com).
    :license: CREATIVE COMMON LICENSE.
    :created at Tue 07 Jun 2022 08:35:04 PM EDT
"""

import csv
import sys


def CheckMatchingDOBs(CSVFile):
    """TODO: Docstring for Check.

    :CSVFile: String of the CSV filename.
    :returns: Number of matching pairs.

    """
    csvreader = csv.reader(open(CSVFile))
    # header = []
    # header = next(csvreader)
    # print(header)

    # Read all rows
    rows = []
    for row in csvreader:
        rows.append(row)

    Count = len(rows)
    print(f"There are {Count-1} students in total.\n")

    # Now find the matching DOBs
    Found = 0
    for i in range(Count):
        for j in range(i+1, Count, 1):
            # print(rows[i][1], rows[j][1], i, j)
            if rows[i][1] == rows[j][1]:
                Found += 1
                print(f"Find matching birthday on {rows[i][1]} for Students {rows[i][0]} and {rows[j][0]}")
    return(Found)


def main():
    # Parse the input CSV filename.
    if len(sys.argv) < 2:
        CSVFile = "DOB.csv"
        print("Checking the test CSV file: DOB_Test.csv.\n")
    else:
        CSVFile = sys.argv[1]

    print(f"\nFound {CheckMatchingDOBs(CSVFile)} pairs of matching birthdays.")


if __name__ == "__main__":
    main()

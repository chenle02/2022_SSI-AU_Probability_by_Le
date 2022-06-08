#!/usr/bin/env python3
# By Le Chen
# chenle02@gmail.com / le.chen@auburn.edu
#
# -*- coding: utf-8 -*-
"""
    codes.GenDOB
    ~~~~~~~~~~~~

    DESCRIPTION

    This code generate random date-of-birth (DOB) uniformly distributed in years from 2005 to 2007 (three consecutive non leap years)

    Usage: GenDOB.py [Number_of_Students|50]

    Output: Output.csv.

    :copyright: (c) 2022 by Le Chen (chenle02@gamil.com).
    :license: CREATIVE COMMON LICENSE.
    :created at Tue 07 Jun 2022 08:14:20 PM EDT
"""
from datetime import date, timedelta
import random
import sys
import csv


def GenDOB(NumStudents, CSVFile):
    """TODO: Docstring for GenDOB.

    :NumStudents: number of student, integer.
    :CSVFile: String for the output csv filename.
    :returns: Output.csv

    """
    with open(CSVFile, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # Write the header to the CSV file
        writer.writerow(["ID", "DOB"])
        # Now generate random DOB's
        for i in range(NumStudents):
            # Random years from 2005 to 2007
            year = random.randint(2005, 2007)
            # Random number between 1 to 365
            day_num = random.randint(1, 365)
            # Initializing start date
            start_date = date(year, 1, 1)
            # converting to date
            res_date = start_date + timedelta(day_num - 1)
            res = res_date.strftime("%m/%d")
            # printing result
            print(f"Random student No. {i+1} is born in {res}, {year}")
            # Save to a CSV file
            writer.writerow([f"No.{i+1}", res, ""])


def main():
    if len(sys.argv) < 2:
        print("Using the default number 46.")
        NumStudents = 46
    else:
        NumStudents = int(sys.argv[1])
    GenDOB(NumStudents, "Output.csv")


if __name__ == "__main__":
    main()

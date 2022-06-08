#!/usr/bin/env python3
# By Le Chen
# chenle02@gmail.com / le.chen@auburn.edu
#
# -*- coding: utf-8 -*-
"""
    codes.BatchTest
    ~~~~~~~~~~~~~~~

    DESCRIPTION

    :copyright: (c) 2022 by Le Chen (chenle02@gamil.com).
    :license: CREATIVE COMMON LICENSE, see LICENSE for more details.
    :created at Tue 07 Jun 2022 09:07:10 PM EDT
"""

from GenDOB import GenDOB
from Checking import CheckMatchingDOBs
import math

NumSuccess = 0
NumTrials = 1000
NumStudents = 15
CSVFile = "Output.csv"

for i in range(NumTrials):
    print(f"Random Group {i+1}\n")
    GenDOB(NumStudents, CSVFile)
    Found = CheckMatchingDOBs(CSVFile)
    print(f"\nFound {Found} pairs of matching birthdays.\n\n---")
    if Found > 0:
        NumSuccess += 1

print(f"""
    *************************************************
    *
    * Among {NumTrials} random classes,
    * with each class having {NumStudents} students,
    * there are {NumSuccess} classes having matching DOBs,
    * which gives {100 * NumSuccess/NumTrials}% of probability of matching.
    *
    * The theoretical rate is {(1-math.factorial(365)/math.factorial(365-NumStudents)/pow(365,NumStudents))*100:.3f}%.
    *
    *************************************************
""")

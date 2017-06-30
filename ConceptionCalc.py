#!/usr/bin/python

import sys

months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

birthMonth = raw_input("Enter your birth month(1-12):")
month = int(birthMonth) - 9
print months[month-1]

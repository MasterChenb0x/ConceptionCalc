#!/usr/bin/python

import sys
import calendar

months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

# Information gathering
birthMonth = raw_input("Enter your birth month(1-12):")
birthDay = raw_input("Enter the day of your birth(1-31):")

momBirthMonth = raw_input("Enter the birth month of your mother(1-12):")
momBirthDay = raw_input("Enter the day of your mother's birth(1-31):")

dadBirthMonth = raw_input("Enter the birth month of your father(1-12):")
dadBirthDay = raw_input("Enter the day of your father's birth(1-31):")

anniversaryMonth = raw_input("Enter the month of your parents' anniversary(1-12):")
anniversaryDay = raw_input("Enter the day of your parents' anniversary(1-31):")


month = int(birthMonth) - 9
print months[month-1]

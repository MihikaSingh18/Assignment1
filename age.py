#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      singh
#
# Created:     04-06-2023
# Copyright:   (c) singh 2023
# Licence:     <your licence>
#------------------------------------------------------------------------------if age >= 18:
age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor")
elif age >= 18 and age < 65:
    print("You are an adult")
else:
    print("You are a senior")

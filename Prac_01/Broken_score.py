"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
elif score >= 90:
    print("Execelent")
elif score < 90:
    print("Passable")
else:
    print("Bad")

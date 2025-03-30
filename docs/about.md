---
layout: page
title: About
permalink: /about/
---

# **Social Data Analysis and Visualization** 

# Assignment 2 - Spring 2025

Group 13
 - Mursal Kakar (s240362)
 - Gisle Joe Garen (s242715)
 - Joachim Rønsholt (233914)



# Contribution 

from tabulate import tabulate

data = [
    ["Alice", 24, "Engineer"],
    ["Bob", 30, "Designer"],
    ["Charlie", 28, "Teacher"]
]

headers = ["Name", "Age", "Profession"]

print(tabulate(data, headers=headers, tablefmt="grid"))

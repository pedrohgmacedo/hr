#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    roundedGrades = []
    for grade in grades:
        nextMultiple = (grade//5+1)*5
        if nextMultiple - grade < 3 and grade >= 38:
            roundedGrades.append(nextMultiple)
        else:
            roundedGrades.append(grade)

    return roundedGrades


if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    print('-'*80)
    result = gradingStudents(grades)
    print('+'*80)
    print(result)

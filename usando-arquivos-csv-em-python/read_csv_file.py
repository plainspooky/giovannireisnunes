#!/usr/bin/env python3
"""
Lê arquivo CSV.
"""
from csv import reader

# arquivo de entrada
STUDENTS_FILE = "students.csv"

if __name__ == "__main__":

    # carrega todas as linhas do arquivo CSV
    with open(STUDENTS_FILE, "r") as f:
        students = [record for record in reader(f)]

    # imprime as duas primeiras colunas de cada registro
    for student in students[1:]:
        print("{0:03d} : {1}".format(int(student[0]), student[1]))

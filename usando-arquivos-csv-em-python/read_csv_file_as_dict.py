#!/usr/bin/env python3
"""
Lê um arquivo CSV para um dicionário.
"""
from csv import DictReader
from json import dumps

# arquivo de entrada
STUDENTS_FILE = "students.csv"

if __name__ == "__main__":

    # carrega todas as linhas do arquivo CSV
    with open(STUDENTS_FILE, "r") as f:
        students = [record for record in DictReader(f)]

    # imprime apenas o nono registro
    print(dumps(students[8], indent=4))

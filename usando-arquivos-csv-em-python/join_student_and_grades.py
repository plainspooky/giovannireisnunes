#!/usr/bin/env python3
"""
Junta dois arquivos CSV criando um terceiro.
"""
from csv import reader, writer

# oa arquivoso que serão lidos/criados
STUDENTS_FILE = "students.csv"
GRADES_FILE = "grades.csv"
JOINED_FILE = "joined.csv"

if __name__ == "__main__":

    # usa o 'with' para abrir todos os arquivos de uma vez
    with open(STUDENTS_FILE, "r") as sf, open(GRADES_FILE, "r") as gf, open(
        JOINED_FILE, "w"
    ) as jf:

        joined = writer(jf)
        students = reader(sf)
        grades = reader(gf)

        # lê uma linha de cada um dos arquivos de entrada...
        for student, grade in zip(students, grades):
            # ...junta e escreve no arquivo de saída
            joined.writerow(student + grade[1:])

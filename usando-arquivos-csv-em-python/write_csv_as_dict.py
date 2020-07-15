#!/usr/bin/env python3
"""
Escreve arquivo CSV a partir de um dicionário.
"""
from csv import DictReader, DictWriter
from random import uniform

# arquivo de entrada
STUDENTS_FILE = "students.csv"
# arquivo de saída
CLASS_FILE = "classes.csv"

# colunas a utilizar no arquivo de entrada
KEYS_TO_KEEP = (
    "id",
    "nome",
)

# nomes da colunas a adicionar
CLASSES = (
    "biologia",
    "educação física",
    "filosofia",
    "física",
    "geografia",
    "história",
    "literatura",
    "língua estrangeira",
    "língua portuguesa",
    "matemática",
    "química",
)

if __name__ == "__main__":

    # gera números aleatórios com duas casas decimais
    grade = lambda: round(uniform(0.0, 10.0), 2)

    with open(CLASS_FILE, "w") as f:
        # instancia o objeto DictWriter
        w = DictWriter(f, fieldnames=list(KEYS_TO_KEEP + CLASSES))
        # grava o cabeçalho
        w.writeheader()
        # lê o arquivo de entrada...
        for student in DictReader(open(STUDENTS_FILE, "r")):
            # escreve uma linha da união de dois dicionários, o primeiro
            # contém apenas as colunas definidas do arquivo de entrada e
            # o segundo contém os valores das novas colunas
            w.writerow(
                {
                    **{key: student[key] for key in KEYS_TO_KEEP},
                    **{class_name: grade() for class_name in CLASSES},
                }
            )

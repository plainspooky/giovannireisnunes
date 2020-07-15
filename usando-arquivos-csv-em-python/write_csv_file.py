#!/usr/bin/env python3
"""
Escreve arquivo CSV.
"""
from csv import writer
from random import uniform

# arquivo de saída
GRADES_FILE = "grades.csv"

# cabeçalho do arquivo CSV
HEADER = ["id", "nota1", "nota2"]

if __name__ == "__main__":

    # gera números aleatórios com duas casas decimais
    grade = lambda: round(uniform(0.0, 10.0), 2)

    # expressão geradora, cria 10 linhas
    data = ((i + 1, grade(), grade()) for i in range(10))

    with open(GRADES_FILE, "w") as f:
        w = writer(f)
        # escreve o cabeçalho
        w.writerow(HEADER)
        # escreve todas as linhas
        w.writerows(data)

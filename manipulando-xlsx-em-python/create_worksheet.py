#!/usr/bin/env python3
from random import randint

from openpyxl import Workbook

RAND = (1, 100)
ROWS, COLS = 10, 10

wb = Workbook()
ws = wb.active

for r in range(1, ROWS + 1):
    for c in range(1, COLS + 1):
        ws.cell(row=r, column=c, value=randint(*RAND))

ws.title = "Aleatório"
wb.save("aleatórios.xlsx")

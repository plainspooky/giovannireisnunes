#!/usr/bin/env python3
"""
Manipula dados de CSV em variáveis e não arquivos.
"""
from csv import reader, writer
from io import StringIO

# este é o arquivo CSV falso
fake_csv_file = (
    "SP,São Paulo\n"
    + "RJ,Rio de Janeiro\n"
    + "ES,Espírito Santo\n"
    + "MG,Minas Gerais\n"
)

if __name__ == "__main__":

    # cria dois opjetos StringIO
    input_file = StringIO(fake_csv_file)
    output_file = StringIO()

    # lê os dados do arquivo CSV e ordena.
    data = sorted(reader(input_file))

    # prepara para gravar o arquivo CSV...
    w = writer(output_file)

    # ...e "grava" um falso arquivo CSV.
    w.writerows(data)

    print(output_file.getvalue())

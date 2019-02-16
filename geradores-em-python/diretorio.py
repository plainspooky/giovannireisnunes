#!/usr/bin/env python3
""" Exemplo de leitura de arquivos de diretórios. """
from os import listdir, path
from fnmatch import fnmatch

ME_IGNORE = ".ignore"
FONTES = "*.txt"


def recupera_arquivos(*lista_de_diretorios):
    """ (Gerador) Recupera os arquivos de uma lista de diretórios. Recebe a
    lista como uma tupla em `lista_de_diretorios` e retorna cada arquivo
    dentro deles. """

    def verifica_diretorio(dirs):
        """ (Gerador) Verifica se o diretório existe e também se o arquivo
        que indica que ele deve ser ignorado existe. """
        for diretorio in dirs:
            me_ignore = path.isfile(path.join(diretorio, ME_IGNORE))
            if path.isdir(diretorio) and not me_ignore:
                yield diretorio

    for diretorio in verifica_diretorio(lista_de_diretorios):
        for arquivo in listdir(diretorio):
            if fnmatch(arquivo, FONTES):
                yield path.join(diretorio, arquivo)


def main():
    """ Função principal. """
    for arquivo in recupera_arquivos("abc", "def", "ghi"):
        print("==> {}".format(arquivo))


if __name__ == "__main__":
    main()

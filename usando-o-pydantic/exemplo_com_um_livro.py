#!/usr/bin/env python3
"""Exemplo com o uso a primeira versão da classe 'Book'
e um único livro."""
import json

from books.models import BookBase as Book


data = json.load(open("livros.json", "r"))
book = Book(**data[0])

print(book.json(indent=4))

#!/usr/bin/env python3
"""Exemplo com a versão final das classes 'Book' e 'Shelf'."""
import json

from books.models import BookV2 as Book
from books.models import ShelfV2 as Shelf


data = json.load(open("livros.json", "r"))
books = [Book(**book) for book in data]

shelf = Shelf(id="d09722d7-a92d-4e79-a972-7b4712abe2c3", books=books)

print(shelf.json(indent=4))

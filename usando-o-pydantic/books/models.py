"""Modelos de exemplo do Pydantic"""
from datetime import datetime
from enum import Enum
from typing import Tuple
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, validator

from .validators import validate_isbn_digit


class BookBase(BaseModel):
    """Classe básica com os dados de livro."""

    id: int
    title: str
    subtitle: str = ""
    author: str


class BookWithValidation(BookBase):
    """Classe de livro que valida autor e título."""

    @validator("title", "author")
    def validate_not_empty(cls, value: str, **kwargs) -> str:
        """Verifica se os campos informados não estão vazios."""
        if value == "":
            raise ValueError("value can't be an empty string")
        return value


class BookWithISBN(BookWithValidation):
    """Classe de livro que valida autor, título e e ISBN."""

    isbn: str

    @validator("isbn")
    def validate_isbn(cls, value: str, **kwargs) -> str:
        """Verifica se o ISBN informado é válido."""
        if not validate_isbn_digit(value):
            raise ValueError("value is not a valid ISBN")
        return value


class LanguageEnum(str, Enum):
    """Idiomas válidos para os livros."""

    en = "English"
    pt = "Portuguese"


class BookWithLanguage(BookWithISBN):
    """Classe de livro com validação e enumeração."""

    language: LanguageEnum = LanguageEnum.pt


class Shelf(BaseModel):
    """Class prateleira para guardar os livros."""

    id: UUID
    books: Tuple[BookWithLanguage, ...]


class BookV2(BaseModel):
    """Segunda versão da classe de livros contento todos os campos dos
    exemplos anteriores e mais alguns novos."""

    id: int
    title: str
    subtitle: str = ""
    author: str
    publisher: str
    pages: int
    isbn: str
    language: LanguageEnum = LanguageEnum.pt

    @validator("title", "author", "publisher")
    def validate_not_empty(cls, value: str, **kwargs) -> str:
        """Verifica se os campos informados não estão vazios."""
        if value == "":
            raise ValueError("value can't be an empty string")
        return value

    @validator("isbn")
    def validate_isbn(cls, value: str, **kwargs) -> str:
        """Verifica se o ISBN informado é válido."""
        if not validate_isbn_digit(value):
            raise ValueError("value is not a valid ISBN")
        return value

    @validator("pages")
    def validate_not_zero(cls, value: int, **kwargs) -> int:
        """Verifica se o número de páginas é maior que 1."""
        if value < 1:
            raise ValueError("number of pages can't be 0 or less")
        return value


class ShelfV2(BaseModel):
    """Class prateleira para guardar os livros."""

    id: UUID
    books: Tuple[BookV2, ...]
    created_at: datetime = datetime.now()

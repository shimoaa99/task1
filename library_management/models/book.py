from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'

    title = fields.Char(string='Title')
    author = fields.Char(string='Author')
    publication_year = fields.Integer(string='Publication Year')
    isbn_number = fields.Char(string='ISBN Number')


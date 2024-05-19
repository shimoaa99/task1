from odoo import http
from odoo.http import request
import json


class BookController(http.Controller):

    @http.route('/books', auth='public', methods=['GET'], type='http')
    def get_books(self, **kwargs):
        books = request.env['library.book'].search([])
        return request.make_response(
            json.dumps([book.read(['id', 'title', 'author', 'publication_year', 'isbn_number']) for book in books]))

    @http.route('/books/add', auth='user', methods=['POST'], type='json', csrf=False)
    def add_book(self, **kwargs):
        data = json.loads(kwargs.get('data'))
        if not data:
            return {'error': 'Missing request body'}
        values = {
            'title': data.get('title'),
            'author': data.get('author'),
            'publication_year': data.get('publication_year'),
            'isbn_number': data.get('isbn_number'),
        }
        request.env['library.book'].create(values)
        return {'status': 'success'}

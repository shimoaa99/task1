{
    'name': 'Library Management',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Manage books in a library.',

    'license': 'AGPL-3',
    'website': 'https://www.example.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

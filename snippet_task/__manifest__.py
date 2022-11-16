{
    'name' : 'Snippet Task',
    'version' : '1.0',
    'sequence': -200,
    'description': "This is for task purpose",
    #'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : ['sale', 'website'],
    'data': [
    'views/snippets/snippet_template.xml',
    'views/snippets/snippet_register.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets': {
        'web.assets_frontend': [
            'snippet_task/static/src/css/my_css.css',
        ]
    }

}
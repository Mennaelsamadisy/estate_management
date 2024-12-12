{
    'name': "estate management",
    'version': '1.0',
    'depends': ['base'],
    'author': "menna",
    'category': 'uncategorized',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/property.xml',
        'views/property_menus.xml'

    ],
    # data files containing optionally loaded demonstration data
    'demo': [

    ],
    'installable': True,
    'application': True
}
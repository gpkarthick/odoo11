{
    'name': 'GPS Location',
    'version': '1.1',
    'category': 'Gendral',
    'summary': 'Get latitude and longitude of my current location',
    'description': """
		Get latitude and longitude of my current location
    """,
    'depends': ['base','mail'],
    'data': [                    
          'views/templates.xml',
          'views/location_view.xml',
		],
    'author': '(Karthick G P)',
    'images': [
        'static/description/icon.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}

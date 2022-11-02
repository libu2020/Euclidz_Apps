{
    'name': 'Fleet Driver Management',
    'version': '14.0.0.1.0',
    'summary': 'Fleet driver management with HR Attendance And Payments',
    'sequence': 10,
    'description': """Fleet driver track with HR Attendance""",
    'category': 'Industries',
    'author': 'Euclidz',
    'maintainer': 'Euclidz Technologies',
    'company': 'Euclidz',
    'website': 'https://euclidz.ai/',
    'license': 'AGPL-3',
    'depends':  ['base', 'account', 'fleet', 'fleet_rental', 'mail', 'hr', 'hr_attendance'],
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_rental_driver_view.xml',
        'data/payment.xml'



    ],
    'demo': [],
    'images': ['static/description/banner.png'],
    'qweb': [],

    'installable': True,
    'application': True,
    'auto_install': False,
}


{
    'name': 'Hospital Management System',
    'author': 'Odoo Mates',
    'website': 'www.odoomates.tech',
    'summary': 'odoo 16 Development',
    'depends': ['mail', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/patient.xml',
        'views/kid.xml',
        'views/patient_gender.xml',
        'views/doctor.xml',
        'views/sale.xml',
    ]
}

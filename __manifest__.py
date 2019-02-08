{
    'name': 'Gestion des formations',
    'summary': """Gestion des formations""",
    'version': '1.0',
    'description': """Ce module est destiné pour gérer un centre de formation.""",
    'author': 'Moussaoui Sara',
    'company': 'Moussaoui Sara',
    'website': 'http://www.moussaoui.com',
    'category': 'Formations',
    'depends': ['base', 'account'],
    'license': 'AGPL-3',
    'data': [
        'views/formation.xml',
		'views/candidat.xml',
		'views/session.xml',
		'views/formateur.xml',
		'views/salle.xml',
		'views/attestation.xml',
		'wizard/attestation.xml',
		'report/report.xml',
		'security/security.xml',
		'security/ir.model.access.csv',
    ],
    
    'installable': True,
    'auto_install': False,

}
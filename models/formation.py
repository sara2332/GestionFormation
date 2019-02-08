from odoo import models,fields

class Formation(models.Model):
	_name = 'formation.formation'

	name = fields.Char(string="Nom")
	prix = fields.Float(string="Prix")
	session_ids = fields.One2many('session.session', 'formation_id', string='session')
	attestation_id= fields.One2many('attestation.attestation','formation_id', string="attestation")
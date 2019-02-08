from odoo import models,fields

class Candidat(models.Model):
	_name = 'candidat.candidat'

	name = fields.Char(string="Nom")
	num_ins = fields.Integer(string="Numero d inscription")
	sessions_ids = fields.Many2many('session.session', string="sessions")
	attestation_id= fields.One2many('attestation.attestation','candidat_id', string="attestation")
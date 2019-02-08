from odoo import models,fields

class Attestation(models.Model):
	_name = 'attestation.attestation'

	date= fields.Date(string="date")
	description = fields.Char(string="description")
	candidat_id= fields.Many2one('candidat.candidat','candidat_id', ondelete="restrict")
	formation_id= fields.Many2one('formation.formation','formation_id', ondelete="restrict")
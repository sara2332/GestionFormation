from odoo import models,fields

class Formateur(models.Model):
	_name = 'formateur.formateur'

	name = fields.Char(string="Nom")
	matricule = fields.Integer(string="Matricule")
	diplome = fields.Char(string="Diplome")
	sessions_ids = fields.Many2many('session.session', string="sessions")
	
	
	
from odoo import models,fields

class Salle(models.Model):
	_name = 'salle.salle'

	name = fields.Char(string="Nom")
	libre = fields.Boolean(string="Places libres")
	nb_place = fields.Integer(string="Nombre de places")
	sessions_ids = fields.Many2many('session.session', string="sessions")
	
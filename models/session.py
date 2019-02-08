from odoo import models,fields,api
from datetime import datetime
from odoo.exceptions import ValidationError

class Session(models.Model):
	_name = 'session.session'
	@api.one
	@api.depends('date_debut','date_fin')
	def compute_dure(self):
		if self.date_debut and self.date_fin:
			date_fin=datetime.strptime(self.date_fin,"%Y-%m-%d")
			date_debut=datetime.strptime(self.date_debut,"%Y-%m-%d")
			self.duree = date_fin - date_debut
		else:
					self.duree=False 

	@api.constrains('date_debut','date_fin')
	@api.depends('date_debut','date_fin')

	def test(self):
		if self.date_debut > self.date_fin:
				raise ValidationError("la date debut ne doit pas etre superieur a date fin")
	
	name = fields.Char(string="Nom")
	nb_participant = fields.Integer(string="Nombre de participants")
	date_debut = fields.Date(string="Date de debut")
	date_fin = fields.Date(string="Date de fin")
	duree = fields.Char(string="Duree")
	state = fields.Selection([('a','A'),('b','B'),('c','C')], string="Etat")
	formation_id = fields.Many2one('formation.formation', string='formationId', ondelete='cascade')
	formateurs_ids = fields.Many2many('formateur.formateur', string="formateurs")
	salles_ids = fields.Many2many('salle.salle', string="salles")
	candidats_ids = fields.Many2many('candidat.candidat', string="candidats")
	
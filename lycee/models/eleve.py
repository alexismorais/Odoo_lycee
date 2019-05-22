#-*- coding: utf-8 -*-

from odoo import models, fields, api

class eleve(models.Model):
    _name = 'lycee.eleve'
    
    firstname = fields.Char("prenom")
    lastname = fields.Char("nom")
    birthday = fields.Date("naissance")
    course_id = fields.Many2one("cours")
    age = fields.Integer("age")
    class_id = fields.Many2one("classe")
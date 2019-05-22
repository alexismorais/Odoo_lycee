#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.fields import Many2many

class classe(models.Model):
    _name = 'lycee.classe'
    
    name = fields.Char("nom")
    level = fields.Char("niveau")
    teacher_id = fields.Many2many("professeur")
    student_ids = fields.One2many("eleve","class_id")
    student_nb = fields.Integer("nombre d'eleve")
#-*- coding: utf-8 -*-

from odoo import models, fields, api

class cours(models.Model):
    _name = 'lycee.cours'
    
    name = fields.Char("nom")
    agenda_ids = fields.One2many("agenda","course_id")

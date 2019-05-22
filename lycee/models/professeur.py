#-*- coding: utf-8 -*-

from odoo import models, fields, api

class professeur(models.Model):
    _name = 'lycee.professeur'
    _inherit = 'res.partner'
    class_ids = fields.Many2many("classe")


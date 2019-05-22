#-*- coding: utf-8 -*-

from odoo import models, fields, api

class professeur(models.Model):
    _name = 'lycee.agenda'

    date_start = fields.Date("debut")
    date_stop = fields.Date("fin")
    room = fields.Char("salle")
    class_id = fields.Many2one("classe")
    course_id = fields.Many2one("cours")


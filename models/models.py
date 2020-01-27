# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class verificaciones_de_productos(models.Model):
#     _name = 'verificaciones_de_productos.verificaciones_de_productos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Revision(models.Model):
    _name = 'verificaciones_de_productos.revision'
    
    #apunte_id = fields.Many2one('verificaciones_de_productos.apunte', ondelete='cascade', string="Apunte", index=True)
    apunte_id = fields.Many2one('verificaciones_de_productos.apunte', ondelete='cascade', string="Apunte", required=True)
    profesional_id = fields.Many2one('res.partner', string="Profesional")
    anotacion = fields.Text(string="Anotacions sobre el apunte")
    

    

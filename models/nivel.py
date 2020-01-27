# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields, api

class Nivel(models.Model):
    _name = 'verificaciones_de_productos.nivel'
    
    nivel_academico = fields.Char(string = "Nivel academico")
    espeificacion = fields.Char(string = "Especificacion")
    descripcion = fields.Text()
    #onde ondelete = 'cascade'
    profesional_id = fields.One2many('res.partner', 'nivel_id', string = "Profesional" )
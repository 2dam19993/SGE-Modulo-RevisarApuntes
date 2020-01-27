# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Apunte(models.Model):
    _name = 'verificaciones_de_productos.apunte'
    
    name = fields.Char(string="Titulo", required="True")
    frase_es_profesional = fields.Char(string="Tipo de apunte",compute='_escribir_el_tipo',store=True)
    description = fields.Text(string="Descripcion",required="True")
    codigo_apunte = fields.Integer(String="Codigo de apunte", required="True")
    es_profesional = fields.Boolean(string="Hecho por un profesional", default=False)
    revisiones_ids = fields.One2many('verificaciones_de_productos.revision','apunte_id', string ="Revisiones")

    
    @api.depends('es_profesional')
    def _escribir_el_tipo(self):
        for a in self:
            if a.es_profesional:
                a.frase_es_profesinal = "Creado por profesinal"
            else:
                a.frase_es_profesinal = "Creado por cliente"

    @api.onchange('apunte','description')
    def _verificar_descipcion(self):
        if self.description and (len(self.description) < 3):
            return {
                'warning': {
                    'title': "Descripción no valido",
                    'message': "La descripción tiene que tener más de 3 caracteres.",
                },
            }

    @api.onchange('apunte','name')
    def _verificar_name(self):
        if self.name and (len(self.name) < 3):
            return {
                'warning': {
                    'title': "Titulo no valido",
                    'message': "El titulo tiene que tener más de 3 caracteres.",
                },
            }
        if self.name and (len(self.name) > 250):
            return {
                'warning': {
                    'title': "Titulo no valido",
                    'message': "El titulo tiene que tener menos de 250 caracteres.",
                },
            }
    
    @api.constrains('apunte','description')
    def _descripcion_correcta(self):
        for a in self:
            if len(a.description)<3:
                raise ValidationError("La descripcion tiene que tener más de 3 caracteres de longitud")
    @api.constrains('apunte','name')
    def _name_correcto(self):
      for a in self:
        if len(a.name)<3:
          raise ValidationError("El titulo tiene que tener más de 3 caracteres de longitud")
        elif len(a.name)>250:
          raise ValidationError("El titulo tiene que tener menos de 250 caracteres de longitud")
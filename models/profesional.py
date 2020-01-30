# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Profesional(models.Model):
    _inherit = 'res.partner'
    
    description = fields.Text(required="True",string="Descripcion")
    contacto = fields.Char(required="True", string="Contacto")
    
    revision_id = fields.One2many('verificaciones_de_productos.revision','profesional_id', string = "Revision" )
    nivel_id = fields.Many2one('verificaciones_de_productos.nivel', ondelete='cascade', string="Nivel")

    @api.onchange('partner','description')
    def _verificar_descipcion(self):
        if self.description and (len(self.description) < 3):
            return {
                'warning': {
                    'title': "Descripción no valida",
                    'message': "La descripción tiene que tener más de 3 caracteres.",
                },
            }
    
    @api.onchange('partner','contacto')
    def _verificar_contacto(self):
        if self.description and (len(self.description) < 3):
            return {
                'warning': {
                    'title': "Contacto no valido",
                    'message': "El contacto tiene que tener más de 3 caracteres.",
                },
            }
    @api.constrains('partner','description')
    def _descripcion_correcta(self):
        for a in self:
            if len(a.description)<3:
                raise ValidationError("La descripcion tiene que tener más de 3 caracteres de longitud")
            elif len(a.description)>250:
                raise ValidationError("La descripcion tiene que tener menos de 250 caracteres de longitud")
    
    @api.constrains('partner','contacto')
    def _contacto_correcto(self):
        for a in self:
            if len(a.contacto)<3:
                raise ValidationError("El contacto tiene que tener más de 3 caracteres de longitud")
            elif len(a.contacto)>100:
                raise ValidationError("El contacto tiene que tener menos de 100 caracteres de longitud")
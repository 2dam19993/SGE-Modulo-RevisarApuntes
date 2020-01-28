# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Revision(models.Model):
    _name = 'verificaciones_de_productos.revision'
    
    #apunte_id = fields.Many2one('verificaciones_de_productos.apunte', ondelete='cascade', string="Apunte", index=True)
    apunte_id = fields.Many2one('verificaciones_de_productos.apunte', ondelete='cascade', string="Apunte", required=True)
    profesional_id = fields.Many2one('res.partner', string="Profesional")
    anotacion = fields.Text(string="Anotacions sobre el apunte",required=True)
    

    @api.onchange('revision','anotacion')
    def _verificar_descipcion(self):
        if self.anotacion and (len(self.anotacion) < 3):
            return {
                'warning': {
                    'title': "Anotación no valido",
                    'message': "La anotación tiene que tener más de 3 caracteres.",
                },
            }
    @api.constrains('revision','anotacion')
    def _descripcion_correcta(self):
        for a in self:
            if len(a.anotacion)<3:
                raise ValidationError("La anotación tiene que tener más de 3 caracteres de longitud")


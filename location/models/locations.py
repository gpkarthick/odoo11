from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError, AccessError

class LocationLatlon(models.Model):
    _name = 'location.latlon'
    _description = 'Location latitude and longitude '
    _order = "name asc"
    
    name = fields.Char('Description', required=True)
    lattitude = fields.Char('Lattitude', required=True)
    longitude = fields.Char('Longitude', required=True)    
    state = fields.Selection([
        ('buttonwork', 'Button Work'),
        ('buttonnotwork', 'Button not work'),    
        ], string='Status')
        
    @api.model
    @api.multi
    def get_gps_location(self,lattitude,longitude, res_id): 
        self.env['location.latlon'].search([('id', '=', res_id)]).write({'lattitude':lattitude,'longitude':longitude})
    
    @api.multi
    def another_button(self): 
        self.write({'state':'buttonwork'})
        self.env['location.latlon'].search([('id', '=', res_id)]).write({'lattitude':lattitude,'longitude':longitude})
       
       
    

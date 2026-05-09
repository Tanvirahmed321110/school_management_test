from odoo import models, fields, api

from python.Lib.email.policy import default


class SchoolFounder(models.Model):
    _name = 'school.founder'
    _description = 'Founder'
    _rec_name = 'name'

    # Basic Information
    name = fields.Char(string='Founder Name', required=True)
    start_journey = fields.Date(string='Start Journey')

    # Description Field
    description = fields.Text(string='Description')
    # Image Field
    image = fields.Image(string='Image')



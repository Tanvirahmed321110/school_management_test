from odoo import models, fields, api

from python.Lib.email.policy import default


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'school student'
    _rec_name = 'name'

    name = fields.Char(string='Student Name', required=True)
    image_1920 = fields.Char(string='Student Image')
    roll = fields.Integer(string='Roll Number',required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender')
    admission_date = fields.Date(string='Admission Date',default=lambda self:fields.Date.today(),required=1)
    class_name = fields.Selection([
        ('six', 'Six'),
        ('seven', 'Seven'),
        ('eight', 'Eight'),
        ('nine', 'Nine'),
        ('ten', 'Ten'),
    ], string='Class', required=True)

    father_name = fields.Char(string="Father's Name")
    mother_name = fields.Char(string="Mother's Name")
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    date_of_birth = fields.Date(string='Date of Birth')

    is_even_roll = fields.Boolean(
        strin='Even Roll',
        compute = '_compute_is_even_roll',
        store=True
    )

    # for  even roll
    @api.depends('roll')
    def _compute_is_even_roll(self):
        for rec in self:
            rec.is_even_roll = rec.roll % 2 ==0
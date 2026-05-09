from odoo import models, fields, api

from python.Lib.email.policy import default


class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'
    _rec_name = 'name'
    _order = 'name'

    # Basic Information
    name = fields.Char(string='Teacher Name', required=True)
    teacher_id = fields.Char(string='Teacher ID', required=True, copy=False, readonly=True,
                             default=lambda self: self.env['ir.sequence'].next_by_code('school.teacher'))
    image_1920 = fields.Image(string='Teacher Image')

    # Personal Information
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)

    # Contact Information
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')

    # Professional Information
    qualification = fields.Char(string='Qualification')
    experience_years = fields.Integer(string='Years of Experience')
    specialization = fields.Char(string='Specialization')
    joining_date = fields.Date(string='Joining Date')

    # Class Related
    class_teacher_of = fields.Selection([
        ('six', 'Six'),
        ('seven', 'Seven'),
        ('eight', 'Eight'),
        ('nine', 'Nine'),
        ('ten', 'Ten'),
    ], string='Class Teacher Of')

    # Salary Information
    basic_salary = fields.Float(string='Basic Salary')
    salary = fields.Float(string='Total Salary', compute='_compute_salary', store=True)

    # Status
    is_active = fields.Boolean(string='Active', default=True)

    # Compute age from date of birth
    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = fields.Date.today()
                age = today.year - record.date_of_birth.year
                if today.month < record.date_of_birth.month or \
                        (today.month == record.date_of_birth.month and today.day < record.date_of_birth.day):
                    age -= 1
                record.age = age
            else:
                record.age = 0



# Model 1: Grade
class TeacherGrade(models.Model):
    _name = 'school.teacher.grade'
    _description = 'Teacher Grade'
    _rec_name = 'name'

    name = fields.Selection([
        ('junior', 'Junior'),
        ('mid', 'Mid'),
        ('senior', 'Senior'),
        ('lead', 'Lead'),
    ], string='Grade', required=True)

    # Grade এর সাথে Salary relation থাকবে Many2many অথবা One2many
    # salary_ids = fields.One2many('teacher.salary', 'grade_id', string='Salaries')
    salary_ids = fields.One2many('school.teacher.salary','grade_id',string='Salaries')


# Model 2: Salary (যেখানে salary থাকবে এবং grade এর সাথে relation থাকবে)
class TeacherSalary(models.Model):
    _name = 'school.teacher.salary'
    _description = 'Teacher Salary'
    _rec_name = 'grade_id'

    # Grade এর সাথে relation (Many2one)
    grade_id = fields.Many2one('school.teacher.grade', string='Grade', required=True)

    # Salary amount
    amount = fields.Float(string='Salary Amount', required=True)


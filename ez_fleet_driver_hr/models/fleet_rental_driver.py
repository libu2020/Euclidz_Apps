from datetime import date, datetime

from odoo import api, fields, models


class FleetRentalDriver(models.Model):
    _inherit = 'car.rental.contract'

    driver_option = fields.Selection([
        ('Vehicle_only', 'Vehicle Only'),
        ('vehicle_driver', 'Vehicle And Driver')
    ], default='Vehicle_only', string="Rental Option", tracking=True,
        help='You can select rental vehicle with or with out driver')
    drivers_id = fields.Many2one('hr.employee', 'Driver', tracking=True, help='Driver of the vehicle', copy=False)
    driver_wage = fields.Float("wage", help="Fixed regular payment for driver")
    payment_ids = fields.One2many("driver.payment", 'payment_id', string="Payment")
    total_salary = fields.Float("Total Salary", compute='_get_total_salary')


    @api.depends('payment_ids')
    def _get_total_salary(self):
        for data in self:
            total_amount = 0
            for value in data.payment_ids:
                total_amount = value.t_salary
            data.total_salary = total_amount

    def driver_payment(self):

        payment = self.env['car.rental.contract'].search([])
        attendance = self.env['hr.attendance'].search([])
        for i in payment:

            today = date.today()
            driver =[]
            d1 = datetime.strptime(str(i.rent_start_date), '%Y-%m-%d').date()
            d2 = datetime.strptime(str(i.rent_end_date), '%Y-%m-%d').date()
            if i.driver_option =="vehicle_driver":
                if (d2 >= today) and (d1 <= today):
                    for j in attendance:

                        if j.worked_hours >= 8.0 and j.employee_id.name == i.drivers_id.name:
                            print("asd")
                            print("gdg", j.worked_hours)

                            driver.append((0, 0, {
                                'date': today,
                                'driver_id': i.drivers_id.id,
                                't_salary': i.driver_wage * (today - d1).days}))

                    i.write(
                        {
                            'payment_ids': driver
                        }
                    )


                else:
                    driver.append((0, 0, {
                        'date': today,
                        'driver_id': i.drivers_id.id,
                        't_salary': i.driver_wage * (today - d1).days - i.driver_wage


                    }))
                    i.write(
                        {
                            'payment_ids': driver
                        }
                    )







class FleetDriverPayment(models.Model):
    _name = "driver.payment"
    _description = "Driver Payment"



    driver_id = fields.Many2one('hr.employee', 'Driver')
    t_salary = fields.Float("Total Salary")
    date = fields.Date("Date")
    payment_id = fields.Float("car.rental.contract")






























# Copyright 2018 ForgeFlow, S.L.
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "HR Attendance Auto Close",
    "version": "14.0.1.0.1",
    "category": "Human Resources",
    "summary": "Close stale Attendances",
    "website": "https://github.com/OCA/hr-attendance",
    "author": "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["hr_attendance_reason"],
    "data": [
        "views/hr_employee.xml",
        "data/hr_attendance_reason.xml",
        "data/hr_attendance.xml",
        "views/hr_attendance_view.xml",
        "views/res_company_view.xml",
    ],
}

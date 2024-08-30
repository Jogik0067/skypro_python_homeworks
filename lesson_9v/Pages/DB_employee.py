from sqlalchemy import create_engine
from sqlalchemy.sql import text


class DBEmployee:
    query = {
        "delete employee": text("DELETE FROM employee "
                                "WHERE id = :new_employee_id"),
        "get company's employees": text("SELECT * FROM employee "
                                        "WHERE company_id = :company_id"),
        "get employee by id": text("SELECT * FROM employee "
                                   "WHERE id = :employee_id"),
        "get max id": text("SELECT MAX(id) FROM employee"),
        "insert new": text("INSERT INTO employee(first_name, last_name, "
                           "phone, company_id, is_active) "
                           "VALUES (:first_name, :last_name, :phone, "
                           ":company_id, :is_active)"),
        "update employee": text("UPDATE employee "
                                "SET email = :new_email, "
                                "is_active = :new_is_active "
                                "WHERE id = :new_employee_id")
    }

    def __init__(self, db_con):
        self.db = create_engine(db_con)

    def create(self, first_name, last_name, phone, company_id, is_active):
        new_employee = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "company_id": company_id,
            "is_active": is_active
        }
        self.db.execute(self.query["insert new"], new_employee)

    def delete(self, id):
        self.db.execute(self.query["delete employee"], new_employee_id=id)

    def get_company_employees(self, new_company_id):
        return self.db.execute(self.query["get company's employees"],
                               company_id=new_company_id).fetchall()

    def get_employee_by_id(self, id):
        return self.db.execute(self.query["get employee by id"],
                               employee_id=id).fetchall()

    def get_max_id(self):
        return self.db.execute(self.query["get max id"]).fetchall()[0][0]

    def update(self, id, email, is_active):
        self.db.execute(self.query["update employee"], new_email=email, 
                        new_is_active=is_active,
                        new_employee_id=id)
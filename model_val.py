from pydantic import BaseModel, Field, field_validator, model_validator, computed_field
from pydantic import EmailStr
from typing import Dict

class Employee(BaseModel):
    name:str
    age:int
    weight:float
    hight:float
    email:EmailStr
    contacts:Dict[str, str]
    salary:float

    @model_validator(mode='after')
    def validate_contacts(cls, model):
        if model.age>60 and 'emergency' not in model.contacts:
            raise ValueError("Emergency contact is required for employees above 60 years")
        return model
    
    @computed_field
    @property
    def cal_bmi(self) -> float:
        bmi = self.weight/self.hight**2
        return round(bmi,2)

def show_employee(employee:Employee):
    print(f"Name: {employee.name}")
    print(f"Age: {employee.age}")
    print(f"Email: {employee.email}")
    print(f"Contacts: {employee.contacts}")
    print(f"BMI: {employee.cal_bmi}")
    print(f"Salary: {employee.salary}")

employee_info = {"name":"Sara Khan","age":70, "weight":60.0, "hight":1.7, "email":"sara12@gmail.com","salary":50000.0, "contacts":{"home":"123456", "work":"987654", "emergency":"112233"}}
employee1 = Employee(**employee_info)
show_employee(employee1) 
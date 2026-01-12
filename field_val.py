from pydantic import BaseModel, EmailStr, field_validator # for custom data validation
from typing import Dict

class Student(BaseModel):
    name:str
    age:int
    email:EmailStr
    contacts:Dict[str, str]

    # for email domain validation
    @field_validator('email')  # mode is 'before' by default and 'after'
    @classmethod
    def validate_email_domain(cls, value):
        valid_domains = ['icic.com', 'hdfc.co', 'uos.pk', 'edu.pk']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valid email domain")
        return value
    
    # for transforming name to uppercase
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    # For checking two or more different fields validation
    
def show_student(student:Student):
    print(f"Name: {student.name}")
    print(f"Age: {student.age}")
    print(f"Email: {student.email}")
    print(f"Contacts: {student.contacts}")
student_info = {"name":"Ali Raza", "email":"ali.raza@uos.pk", "age":20, "contacts":{"home":"123456", "work":"987654"}}
student1 = Student(**student_info)
show_student(student1)

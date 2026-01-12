from pydantic import BaseModel, AnyUrl, EmailStr, Field # for custom data validation
# from pydantic import field_validator
from typing import Optional, List, Dict, Annotated # for type hinting

# this is out template for patient data type validation
class Patient(BaseModel):

    name:str = Field(max_length=30) # name should not exceed 30 characters

    father_name :Annotated[str, Field(max_length=30, title="Father's Name", description="name should not exceed 30 characters")] # another way of defining field with title

    email:EmailStr  # validation for email format

    age:Annotated[int,Field(ge=18, le=60, strict=True)] # age should be between 18 and 60 strict type checking

    linked_in:AnyUrl # validation for URL format

    height:float = Field(ge=3, le=6) # height should be between 3.0 ft to 6.0 ft

    merried:bool = False

    study:Annotated[bool, Field(default=False, description="Is the patient studying?")] # another way of defining field with default value

    allergies:Optional[List[str]] = None #making it optional other fields are mandatory

    contacts:Dict[str, str] = Field(max_length=4) # dictionary to store contact numbers not more than 4

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.height)
    print(patient.merried)
    print(patient.allergies)
    print("Patient data inserted successfully")

patient_info = {"name":"Muhammad Awais", "email":"abc12@gmail.com", "age":25, "linked_in":"https://www.linkedin.com/in/muhammad-awais", "height":5.6, "contacts":{"home":"123456", "work":"987654"}}
patient1 = Patient(**patient_info)
insert_patient_data(patient1)



from pydantic import BaseModel, EmailStr

class Address(BaseModel):
    state:str
    city:str
    pin:str

class Student(BaseModel):
    name:str
    age:int
    email:EmailStr
    address:Address

address_dict = {'state':'Punjab','city':'Chichawatni', 'pin':'57200'}
address_obj = (Address(**address_dict))
student_dict = {'name':'Awais', 'age':25, 'email':'patient2@gmail.com','address':address_dict}
student_obj = Student(**student_dict)

print(student_obj)
print(student_obj.address.city)
print(student_obj.address.pin)


# for exporting model schema in dictionary format
student_obj.model_dump(include=['name','age'], exclude={'address':['state','pin']})

from pydantic import BaseModel

class Patient(BaseModel):

    name: str
    age: int

def insert_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted')

def update_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('Updated')

patient_info ={'name':'Ram', 'age':30}
patient1 = Patient(**patient_info)

insert_patient(patient1)
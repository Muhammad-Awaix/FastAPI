from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

# Load patient data from JSON file
def load_data():
    with open("patients.json","r") as f:
        data = json.load(f)

    return data 

@app.get("/")
def hello():
    return {"message": "Welcome to the Patient Management API"}

@app.get("/about")
def about():
    return {"message": "This API manages patient records and information."}

# view all patients
@app.get('/view')
def view():
    data  = load_data()
    return data 


# for specific patient Path parameter
@app.get('/patient/{p_id}')
def get_patient(p_id:str = Path (..., description="The ID of the patient to retrieve", example="P001")):
    data  = load_data()
    if p_id in data:
        return data[p_id]
    raise HTTPException(status_code = 404, detail = "Patient not found")

# Query parameter example
@app.get('/sort')
def sort_patient(sort_by: str = Query(..., description = "sort on the basis of hight, weight, bmi"),order:str = Query('asc', description="Order of sorting: asc or desc")):

    valid_fields = ['height', 'weight', 'bmi']
    valid_order = ['asc', 'desc']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field selected from {valid_fields}")
    if order not in valid_order:
        raise HTTPException(status_code=400, detail="Order must be 'asc' or 'desc'")

    data  = load_data()
    sort_order = True if order == 'desc' else False
    sort_data = sorted(data.values(), key = lambda x:x.get (sort_by, 0), reverse=sort_order)

    return sort_data

from pydantic import BaseModel
from datetime import date

class FacultyCreate(BaseModel):
    name: str
    department : str
    designation : str
    contact:str
    qualifications:str
    experience:int
    doj : date

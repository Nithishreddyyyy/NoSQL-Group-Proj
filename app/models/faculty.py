from pydantic import BaseModel
from datetime import date

class FacultyApp(BaseModel):
    name: str
    department : str
    designation : str
    contact:str
    qualifications:str
    experience:int
    doj : date

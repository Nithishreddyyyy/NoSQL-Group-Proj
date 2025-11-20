from pydantic import BaseModel
from datetime import datetime

class FacultyApp(BaseModel):
    name : str
    desig : str
    contact : str
    qualification : list[str]
    experience : int
    doj : datetime
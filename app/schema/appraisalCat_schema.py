from pydantic import BaseModel

class CriteriaCreate(BaseModel):
    category : str
    name : str
    weifght : float


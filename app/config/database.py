from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["faculty_appraisal"]

faculty_collection = db["faculty"]
criteria_collection = db["criteria"]
documents_collection = db["documents_metadata"]
scores_collection = db["scores"]

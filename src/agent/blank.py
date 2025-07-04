from langchain.chat_models import init_chat_model
import os
from pymongo import MongoClient
from agent.newquestions import questions
from dotenv import load_dotenv
from datetime import datetime
from agent.step2_questions import values
load_dotenv()

# MongoDB connection URI (default to localhost)
try:
    # MongoDB connection URI (default to localhost)
    mongo_uri = os.getenv("MONGODB_URI")
    print(mongo_uri)
    client = MongoClient(mongo_uri)
    # query_filter = {
    #     "topic": "Biochemistry"
    # }
    # update_operation = {
    #     "$set": {
    #         "created_at": datetime.now().isoformat(),
    #         "source": "gpt-4.1"
    #     }
    # }
    db = client["Qbank"]
    collection = db["qbanks"]   # Use your desired database name
    print("MongoDB client set up. Database name:", db.name)
    collection.insert_many(values)
    # collection.update_many(query_filter, update_operation)

    # Remove the 'questions' field from all documents
    # result = collection.update_many({}, {"$set": {"examType": "Step-1"}})
    print(f"Inserted {len(values)} documents.")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
    db = None
    collection = None







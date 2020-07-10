from motor.motor_asyncio import AsyncIOMotorClient
from umongo import Instance

# Connect to Mongodb
MONGO_CLIENT = AsyncIOMotorClient('mongodb://user:password@ip_address')
database = MONGO_CLIENT['test_database']
instance = Instance(database)

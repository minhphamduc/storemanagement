from motor.motor_asyncio import AsyncIOMotorClient
from umongo import Instance

# Connect to Mongodb
MONGO_CLIENT = AsyncIOMotorClient('mongodb://root:123456@192.168.99.100')
database = MONGO_CLIENT['users']
instance = Instance(database)

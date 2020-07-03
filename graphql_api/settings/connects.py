from motor.motor_asyncio import AsyncIOMotorClient
from umongo import Instance


# Khởi tạo kết nối đến MongoDB
MONGO_CLIENT = AsyncIOMotorClient('mongodb://root:123456@192.168.99.100')
MONGO_DATABASE = MONGO_CLIENT['graphql_api']

# Khởi tạo uMongo instance
MONGO_INSTANCE = Instance(MONGO_DATABASE)

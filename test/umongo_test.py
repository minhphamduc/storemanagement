import asyncio
from umongo import Document, fields
from bson.objectid import ObjectId
from aiodataloader import DataLoader
from motor.motor_asyncio import AsyncIOMotorClient
from umongo import Instance

# Connect to Mongodb
MONGO_CLIENT = AsyncIOMotorClient('mongodb://user:password@ip_address')
database = MONGO_CLIENT['test_database']
instance = Instance(database)


# umongo document object
@instance.register
class Persons(Document):
    fullname = fields.StringField()

    class Meta:
        collection_name = "persons"


@instance.register
class Users(Document):
    username = fields.StringField()
    best_friend = fields.ReferenceField(document=Persons)
    friends = fields.ListField(fields.ReferenceField(document=Persons))

    class Meta:
        collection_name = "users"


class UserLoader(DataLoader):
    # Batch funciton
    @staticmethod
    async def get_users(keys):
        tasks = []
        for key in keys:
            tasks.append(
                await Users.find_one({'_id': ObjectId(key)})
            )
        return tasks

    async def batch_load_fn(self, keys):
        return await self.get_users(keys)


async def test_dataloader(keys):
    identity_loader = UserLoader()

    promise_all = []
    for key in keys:
        test = identity_loader.load(key)
        promise_all.append(test)


# Grab event loop
loop = asyncio.get_event_loop()

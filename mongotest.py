import pymongo
client = client = pymongo.MongoClient("mongodb+srv://shubham:Shubham#123@cluster0.bo624dn.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "Shubham",
    "email": "shubham@gmail.com",
    "surname": "Pandit"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
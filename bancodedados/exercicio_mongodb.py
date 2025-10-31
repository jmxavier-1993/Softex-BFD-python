import pymongo

conn= pymongo.MongoClient("")

print(conn)

conn.close()
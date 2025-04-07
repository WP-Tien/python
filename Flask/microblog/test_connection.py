from pymongo import MongoClient

try:
    uri = "mongodb+srv://nguyenhuutienit3895:57X4q46WcEgSPNRd@cluster0.xwlvt.mongodb.net/"
    client = MongoClient(uri)

    client.admin.command("ping")
    print("Connected successfully")

    client.close()
except Exception as e:
    raise Exception(
        "The following error occurred: ", e)

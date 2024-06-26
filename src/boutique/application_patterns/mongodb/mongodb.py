"""
download mongodb
create the following directories for your project
data
data/db
data/logpython

pip install pymongo
works bestr in container - docker pull mongo
"""
from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, host='127.0.0.1', port=27017):
        """
        be sure to use the ip address not name for local windows
        CAUTION: Don't do this in production!!!
        """

        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.host, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


def print_mdb_collection(collection_name):
    for doc in collection_name.find():
        print(doc)

def main():
    mongo = MongoDBConnection()

    with mongo:
        # mongodb database; it all starts here
        db = mongo.connection.media

        # collection in database
        cd = db["cd"]

        # notice how easy these are to create and that they are "schemaless"
        # that is, the Python module defines the data structure in a dict,
        # rather than the database which just stores what it is told

        cd_ip = {"artist": "The Who", "Title": "By Numbers"}
        result = cd.insert_one(cd_ip)

        cd_ip = [
            {"artist": "Deep Purple", "Title": "Made In Japan", "name": "Andy"},
            {"artist": "Led Zeppelin", "Title": "House of the Holy", "name": "Andy"},
            {"artist": "Pink Floyd", "Title": "DSOM", "name": "Andy"},
            {"artist": "Albert Hammond", "Title": "Free Electric Band", "name": "Sam"},
            {"artist": "Nilsson", "Title": "Without You", "name": "Sam"}
        ]
        result = cd.insert_many(cd_ip)

        print_mdb_collection(cd)

        collector = db["collector"]
        collector_ip = [
            {"name": "Andy", "preference": "Rock"},
            {"name": "Sam", "preference": "Pop"}
        ]

        result = collector.insert_many(collector_ip)
        print_mdb_collection(collector)

        for name in collector.find():
            print(f'List for {name["name"]}')
            query = {"name": name["name"]}
            for a_cd in cd.find(query):
                print(f'{name["name"]} has collected {a_cd}')

        yorn = input("Drop data?")
        if yorn.upper() == 'Y':
            cd.drop()
            collector.drop()


if __name__ == "__main__":
    main()   

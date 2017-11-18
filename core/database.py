from pymongo import MongoClient


def get_client():
    return MongoClient('mongodb://underpriced:mongounderpriced@localhost/underpriced?authMechanism=SCRAM-SHA-1')
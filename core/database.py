from pymongo import MongoClient


def get_client():
    return MongoClient('mongodb://underpriced:mongounderpriced@104.214.239.181/underpriced?authMechanism=SCRAM-SHA-1')

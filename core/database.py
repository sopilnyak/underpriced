from pymongo import MongoClient


def get_client():
    return MongoClient('mongodb://underpriced:mongounderpriced@46.101.112.24/underpriced?authMechanism=SCRAM-SHA-1')
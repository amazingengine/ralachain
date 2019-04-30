import json

JSON_FILE_PATH = '../test/mocks/redis_testdata.json'


def insert_testdata_to_redis(redis_reader):
    with open(JSON_FILE_PATH, 'r') as json_file:
        dict_json = json.load(json_file)
        for k in dict_json:
            redis_reader.redis.hmset(k, dict_json[k])


def delete_testdata_to_redis(redis_reader):
    with open(JSON_FILE_PATH, 'r') as json_file:
        dict_json = json.load(json_file)
        for k in dict_json:
            redis_reader.redis.delete(k)

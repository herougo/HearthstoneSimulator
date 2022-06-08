import uuid

NULL_HASH = -1
PLAYER0_HASH = 0
PLAYER1_HASH = 1
LAST_HASH = 1

def _generate_random_hash_v2(hash_dict=None):
    while True:
        my_hash = uuid.uuid4().hex
        if hash_dict is None or my_hash not in hash_dict.keys():
            return my_hash

def generate_random_hash():
    global LAST_HASH
    LAST_HASH += 1
    return LAST_HASH
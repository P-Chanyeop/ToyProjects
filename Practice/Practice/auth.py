def login(_id):
    members = ['egoing', 'yeop', 'leezche']
    for member in members:
        if member == _id:
            return True
    return False

from operator import attrgetter


class User(object):
    """docstring for User"""

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(21), User(2), User(33)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))
    print(sorted(users, key=attrgetter('user_id')))


if __name__ == '__main__':
    sort_notcompare()

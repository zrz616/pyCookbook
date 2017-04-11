from operator import itemgetter
import pprint

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
pp = pprint.PrettyPrinter(indent=4, depth=2)
pp.pprint(sorted(rows, key=itemgetter('fname')))
pp.pprint(sorted(rows, key=itemgetter('uid')))
pp.pprint(sorted(rows, key=itemgetter('lname', 'fname')))

pp.pprint(sorted(rows, key=lambda r: r['fname']))
pp.pprint(min(rows, key=itemgetter('fname')))

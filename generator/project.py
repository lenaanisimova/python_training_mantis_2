from model.project import Project
import random
import string
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
n = 5
f = "data/project.json"
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = Project(name=random_string("project_name", 10),
                   status=random.choice(["development", "release", "stable", "obsolete"]),
                   view_status=random.choice(["private", "public"]),
                   description=random_string("description", 10),
                   inherit_global_categories=random.choice([True, False]))

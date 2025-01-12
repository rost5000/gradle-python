import datetime
import math
import os
import random
from git import Repo

base_file = "../resources/dummy_file.txt"
base_file_path = os.path.abspath(base_file)


repo = Repo('../../../')
start_date = datetime.datetime.now(datetime.UTC)
lambda_exp = 10

def exp_dist(value):
    res = lambda_exp * math.exp(value)
    return 24 if res > 24 else res

end_date = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=5)
delta = datetime.timedelta(days=1)
index = repo.index

while start_date >= end_date:
    date_tmp = start_date
    next_date = start_date - delta

    while date_tmp >= next_date:
        with open(base_file_path, "wt") as f:
            f.write(start_date.__str__())
        index.add([base_file_path])
        index.commit("A commit message", commit_date=date_tmp, author_date=date_tmp)
        date_tmp -= datetime.timedelta(hours=exp_dist(random.random()))
    start_date = next_date
import datetime

import os
from git import Repo

base_file = "../resources/dummy_file.txt"
base_file_path = os.path.abspath(base_file)


repo = Repo('../../../')
start_date = datetime.datetime.now(datetime.UTC)

end_date = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=5)
delta = datetime.timedelta(days=1)
index = repo.index

while start_date >= end_date:
    with open(base_file_path, "wt") as f:
        f.write(start_date.__str__())
    index.add([base_file_path])
    index.commit("A commit message", commit_date=start_date, author_date=start_date)
    start_date -= delta
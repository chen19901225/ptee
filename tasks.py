import os

import re

from invoke import task

proj_name = 'ptee'
proj_dir = os.path.dirname(os.path.abspath(__file__))
python = os.path.join(proj_dir, 'venv/bin/python')


def get_branch_name(c):
    out = c.run("git branch")
    # print(out)
    lines = out.stdout.splitlines()
    if not lines:
        return 'master'
    current_branch_line = [ele for ele in lines if ele.startswith("*")][0]
    print(current_branch_line)
    current_branch = re.split(r"\s+", current_branch_line)[-1]
    return current_branch


@task
def c_push(c):
    branch_name = get_branch_name(c)
    c.run("git push origin {}".format(branch_name))

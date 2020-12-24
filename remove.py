import sys
import os
import subprocess
from config import path, username, token
from github import Github

reponame = sys.argv[1]
dir_path = os.path.dirname(os.path.realpath(__file__))

def remove():
    gh = Github(login_or_token=token)
    repo = gh.get_repo(r'Rage997/' + reponame)
    try:
        repo.delete()
    except Exception as e:
        print(e)
    # Delete the project from the computer. This is dangerous, maybe should provide a parameter
    subprocess.run('rm -rf ' + reponame, shell=True, cwd=path)

if __name__ == "__main__":
    remove()

import sys
import os
import subprocess
from github import Github
from config import path, username, password, token


def newProject(projectName):
    os.makedirs(os.path.join(path + projectName))
    user = Github(login_or_token=token).get_user()
    print(user)
    login = user.login
    print(user)
    repo = user.create_repo(projectName)
    print("Succesfully created a new github project {}".format(projectName))

def initProject(working_directory):
    subprocess.run('pwd', shell=True, cwd=working_directory)
    subprocess.run('git init', shell=True, cwd=working_directory)
    subprocess.run('git remote add origin git@github.com:'+username +'/' + projectName + '.git', shell=True, cwd=working_directory)
    subprocess.run('touch README.md', shell=True, cwd=working_directory)
    subprocess.run('git add .', shell=True, cwd=working_directory)
    subprocess.run('git commit -m \"Initial commit\"', shell=True, cwd=working_directory)
    subprocess.run('git push -u origin master', shell=True, cwd=working_directory)

if __name__ == "__main__":

    projectName = str(sys.argv[1])
    newProject(projectName)
    subprocess.run('cd ' + path + projectName, shell=True)
    working_directory = path + projectName
    initProject(working_directory)

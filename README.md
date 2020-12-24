### Crealete

A python script meant to automate the process of create and delete Github repositories


### Installation

1) Run ```pip install -r requirements.txt ``` 
2) Install crhomedriver https://chromedriver.chromium.org/)
3) Setup your git credentials and the path to your project folder in config.py. You will need to generate a github token https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token and tick the options: repo, delete_repo

If you run on Linux, you can install the chromedriver automatically by ```./install_chromedriver.sh```

### Run

To create a new project: ```./create.py <Name of the project>```
  
To remove a project ```./remove.py <Name of the project>```

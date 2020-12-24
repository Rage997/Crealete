
from github import Github

token = '75121190532e0d606151141f62206df1c0e1e89e'
password = 'Efaage7568850'

user = Github(login_or_token=token, base_url = 'https://api.github.com').get_user()
print(user)
login = user.login
print(user)

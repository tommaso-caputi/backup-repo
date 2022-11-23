from github import Github
from dotenv import load_dotenv
import os
import urllib3

load_dotenv()
ACCESS_TOKEN = os.getenv('TOKEN')

g = Github(ACCESS_TOKEN)

repos = g.get_user().get_repos()

repo = repos[0]

http = urllib3.PoolManager()
r = http.request('GET', "https://api.github.com/repos/"+g.get_user()+"/"+repo+"/contents/", preload_content=False, headers={'Authorization': "token " + ACCESS_TOKEN})
with open("/tmp/master.zip", 'wb') as out:
    while True:
        data = r.read(64)
        if not data:
            break
        out.write(data)
r.release_conn()
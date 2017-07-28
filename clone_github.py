import requests
import simplejson
import subprocess


r2 = requests.get('https://github.ubc.ca/api/v3/users/ubc-mds-2016/repos?access_token=***')
c2 = r2.content
j2 = simplejson.loads(c2)


# r3 = requests.get('https://github.ubc.ca/api/v3/search/repositories?access_token=***')
# c3 = r3.content
# j3 = simplejson.loads(c3)

repo_list = []

for item in j2:
    print(item['git_url'])
    repo_list.append(item['git_url'])
    # print(len(repo_list))

#
# for item in repo_list:
#     subprocess.Popen(['git', 'clone', str(item)])

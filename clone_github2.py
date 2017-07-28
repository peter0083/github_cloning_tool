import github3

g = github3.github.GitHubEnterprise(url='https://github.ubc.ca',
                                    username='***',
                                    password='***',
                                    token='***')

for item in g.search.RepositorySearchResult():
    print(item)

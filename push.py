import git

repo = git.Repo()
repo.git.commit('.','-m','via pygit')
origin = repo.remote(name='origin')
origin.push()

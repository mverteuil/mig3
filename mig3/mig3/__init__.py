import git


def get_version():
    try:
        repository = git.Repo(search_parent_directories=True)
        return repository.head.object.hexsha[:8]
    except git.InvalidGitRepositoryError:
        return "N/A"

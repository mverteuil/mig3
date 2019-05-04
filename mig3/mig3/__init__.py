import git


def get_version():
    """Retrieve current 8-byte git commit SHA, or N/A if not in a repository for some unexplainable reason."""
    try:
        repository = git.Repo(search_parent_directories=True)
        return repository.head.object.hexsha[:8]
    except git.InvalidGitRepositoryError:
        return "N/A"

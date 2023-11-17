import os
import git
from core.common_directories import COMMON

def search_dir(dir):
    """
    Search for repositories in a directory.
    """
    if dir.lower() in COMMON.keys():
        dir = COMMON[dir.lower()]['win']
    repos = {}
    for root, dirs, files in os.walk(dir):
        if '.git' in dirs:
            root_abs = os.path.abspath(root)
            repo_name = get_repo_name(root_abs)
            repos[root_abs] = repo_name
            dirs.remove('.git')
    return repos


def get_repo_name(repo_path):
    """
    Get the name of the repository.
    """
    try:
        repo = git.Repo(repo_path)
        remote_url = next(repo.remote("origin").urls)
        if remote_url.endswith('.git'):
            remote_url = remote_url[:-4]
        return remote_url.split('/')[-1]
    except Exception as e:
        print(f"Error: {e}")
        return None
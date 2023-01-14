import time
import git
import pathlib
import sys


def wasItRufus(git_dir):
    if not pathlib.Path(git_dir).exists():
        print('.git file not found, please check path')
        return
    repo = git.Repo(git_dir)
    repo.config_reader()
    headcommit = repo.head.commit
    date = headcommit.authored_date
    cur = time.time()
    inOneWeek = (cur - date) <= 604800
    print('active branch:', repo.active_branch)
    print('local changes:', repo.is_dirty())
    print('recent commit:', inOneWeek)
    print('blame Rufus:', headcommit.author.name == 'Rufus')


if __name__ == '__main__':
    # change with your .git file path
    git_dir = '/Users/dukaixuan/PycharmProjects/WasItRufus/.git'
    if len(sys.argv) >= 2 and sys.argv[1]:
        git_dir = sys.argv[1]
    print(git_dir)
    wasItRufus(git_dir)

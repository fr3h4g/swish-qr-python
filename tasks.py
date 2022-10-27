from invoke import run, task


@task
def linters(c):
    """Run code linters"""
    run("tox -e linters")

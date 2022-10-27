from invoke import task


@task
def lint(c):
    c.run("flake8 src/swish_qr tests")
    c.run("black src/swish_qr tests --check")


@task
def test(c):
    c.run("pytest --cov=swish_qr  --cov=tests --cov-report=xml tests")

from invoke import task


@task
def lint(c) -> None:
    target = 'dstools'
    print("calling isort")
    c.run(f"isort {target}")
    print("calling black")
    c.run(f"black {target}")
    print("calling flake8")
    c.run(f"flake8 {target}")
    print("calling mypy")
    c.run(f"mypy {target}")


@task
def pip_compile(c) -> None:
    c.run("pip-compile --extra local")
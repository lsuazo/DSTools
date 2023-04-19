from distutils.core import setup

setup(
    name="dstools",
    version="0.1",
    install_requires=[
        "matplotlib",
        "numpy",
        "pandas",
    ],
    extras_require={
        "local": ["black", "flake8", "invoke", "isort", "mypy", "pytest"],
    },
)

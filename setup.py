from setuptools import setup

setup(
    name="Python Bash",
    version="1.0",
    py_modules=["bash"],
    install_requires=[
        "Click",
    ],
    entry_points='''
        [console_scripts]
        pybash=bash:cli
    ''',
)
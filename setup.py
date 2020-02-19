from setuptools import setup

setup(
    name="Python Bash",
    version="1.0",
    py_modules=["bash"],
    install_requires=[
        "Click",
        'odooly'
    ],
    entry_points='''
        [console_scripts]
        pybash_conectar=bash:conectar_servidor
        pybash_odoo=bash:odoo
        pybash_db=bash:duplicar_base
    ''',
)
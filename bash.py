import click

# Definir grupo de comandos
#
#

@click.group()
@click.option('--crear_cuenta', default=False)
def group_cli(crear_cuenta):
    pass

@group_cli.command()
def cli():
    click.echo("Servidor")

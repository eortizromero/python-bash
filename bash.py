import click
import odooly

# Definir grupo de comandos
#
#


@click.command()
@click.argument('servidor', default="localhost")
def conectar_servidor(servidor):
    servidor = click.prompt("Servidor")
    click.echo("{}".format(servidor))


'''
    Comandos para Administrar Odoo 
    __Author__: Edgardo Ortiz
'''


@click.command()
@click.option('--crear-usuario')
def odoo(crear_usuario):
    email = click.prompt('Usuario o Correo')
    password = click.prompt("Contraseña")
    click.echo("%s %s " % (email, password))


@click.command()
def duplicar_base():
    db = click.prompt('Base de datos a duplicar')
    db_duplicate = click.prompt('Nueva base de datos')
    if db == db_duplicate:
        click.echo("Error al duplicar la base de datos, la nueva base debe tener otro nombre.")
        return 
    servidor = click.prompt("Servidor Odoo o IP")
    try:
        servidor = 'http://' + servidor + ':8069'
        client = odooly.Client(servidor)
    except Exception as e:
        raise Warning("%s " % e)

    list_dbs = client.db.list()
    if not db in list_dbs:
        click.echo("La base de datos %s, no existe." % db)
        return
    
    click.echo("Bases de datos %s" % list_dbs)

    #user = click.prompt("Usuario Odoo")
    #password =  click.prompt("Contraseña Odoo")

    click.echo("Duplicando base %s a %s" % (db, db_duplicate))
    
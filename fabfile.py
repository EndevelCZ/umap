import os
import datetime
from fabric.api import prefix, env, run
from fabric.decorators import task, hosts
from fabric.colors import blue

"""
CONFIG, ENVIROMENTS
"""


TS = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
env.forward_agent = True
env.use_ssh_config = True


@task
@hosts('poznejlanskroun')
def deploy(upgrade_pip=0, migrate=0, collectstatic=1):
    _deploy(upgrade_pip, migrate, collectstatic)


def _deploy(upgrade_pip=0, migrate=0, collectstatic=1):

    with prefix('source %s' % os.path.join('/', 'srv', 'umap', 'venv', 'bin', 'activate')):

        if bool(int(upgrade_pip)):
            run('pip install -U pip setuptools wheel')

#            run('pip install -U -r requirements/base.txt')
        run('pip install git+https://github.com/EndevelCZ/umap --upgrade')

        if bool(int(collectstatic)):
            print(blue('Collecting static files...'))
            run('umap collectstatic --noinput')

        # print(blue('Compiling project own translation files...'))
        # with prefix('cd frc'):
        #     run('django-admin compilemessages')

        if bool(int(migrate)):
            print(blue('Running migrations...'))
            run('%s migrate' % env.manage_cmd)

    run('service uwsgi restart')

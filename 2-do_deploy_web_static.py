#!/usr/bin/python3
'''
Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy
'''
from fabric.api import env
from fabric.api import run
from fabric.api import local
from fabric.api import put
from datetime import datetime
from os import path


env.hosts = ['100.26.241.94', '35.168.1.10']


def do_pack():
    '''
    generates a .tgz archive from the contents of the web_static folder
    '''
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}.tgz".format(time_stamp)

    # create versions folders if it does not exist
    local("mkdir -p versions")
    full_path_to_archive = "versions/{}".format(file_name)

    # Create archive of web_static
    archive = local("tar -czvf {} web_static".format(full_path_to_archive))

    if archive.succeeded:
        return (full_path_to_archive)
    else:
        return (None)


def do_deploy(archive_path):
    '''
    function used to distribute the archives to the web servers
    '''
    if not path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split('/')[-1]
        folder_name = file_name.split('.')[0]
        release_path = '/data/web_static/releases/{}'.format(folder_name)

        if path.exists(release_path):
            run('rm -rf {}/'.format(release_path))

        put(local_path=archive_path, remote_path='/tmp/')

        run('mkdir -p {}'.format(release_path))
        run('tar -zxvf /tmp/{} -C {}'.format(file_name, release_path))
        run('mv {}/web_static/* {}'.format(release_path, release_path))
        run('rm -rf {}/web_static/'.format(release_path))

        run('rm /tmp/{}'.format(file_name))

        current_link = '/data/web_static/current'
        run('rm -f {}'.format(current_link))

        run('ln -s {} {}'.format(release_path, current_link))

        return True
    except Exception as e:
        return False

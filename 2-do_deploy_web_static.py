#!/usr/bin/python3
'''
Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy
'''
from fabric.api import env, run, local, put
from os import path

env.hosts = ['100.26.241.94', '35.168.1.10']


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

        # Upload archive
        put(local_path=archive_path, remote_path='/tmp/')

        # Extract archive
        run('mkdir -p {}'.format(release_path))
        run('tar -zxvf /tmp/{} -C {}'.format(file_name, release_path))

        # delete archive from web servers
        run('rm /tmp/{}'.format(file_name))

        #  delete existing symbolic link to /data/web_static/current
        current_link = '/data/web_static/current'
        run('rm -f {}'.format(current_link))

        # create new symbolic link
        run('ln -s {} {}'.format(release_path, current_link))

        return True
    except Exception as e:
        return False

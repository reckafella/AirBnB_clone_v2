#!/usr/bin/python3
'''
Module containing a function that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,\
    using the function do_pack.

* Prototype: def do_pack():
* All files in the folder web_static must be added to the final archive
* All archives must be stored in the folder versions (your function should\
    create this folder if it doesn’t exist)
* The name of the archive created must be\
    web_static_<year><month><day><hour><minute><second>.tgz
* The function do_pack must return the archive path if the archive\
    has been correctly generated. Otherwise, it should return None
'''
from datetime import datetime
from fabric.api import local


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

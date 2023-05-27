Role Name
=========

Install and configure CTFd service.

Requirements
------------

You need to configure a database and a redis server.
You also need to configure a web server to serve the CTFd application after installation.

Role Variables
--------------

see defaults/[main.yml](defaults/main.yml)

Dependencies
------------

This role dosn't have any dependencies.
But you need to configure a database and a redis server.

Example Playbook
----------------

    - hosts: ctfd
      roles:
         - { role: msterhuj.ctfd }

License
-------

MIT

Author Information
------------------

Created by msterhuj

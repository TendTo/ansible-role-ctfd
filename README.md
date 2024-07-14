CTFD
=========

Install and configure CTFd app

Requirements
------------

You need to configure a database and a redis server.
You also need to configure a web server to serve the CTFd application after installation with nginx proxy.

Role Variables
--------------

Variable can be found in `defaults/main.yml` and are as follows: [Click here](defaults/main.yml)

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

GNU GPLv3

Author Information
------------------

msterhuj <gabin.lanore@gmail.com>

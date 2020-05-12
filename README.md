# WebRTC peers project roles

This repo contains
Ansible roles to install
a simple WebRTC signaling service
on the [stack-deploy](https://github.com/tessercat/stack-deploy) stack.

The [peers-installer](https://github.com/tessercat/peers-installer) repo
uses this repo
to simplify automatic configuration
of the stack and peer service
on an Ubuntu 20.04 host.


## Overview

The target platform
is Ubuntu 20.04 LTS.

The Django project runs
as a systemd service
on a localhost port
in daphne
in a Python 3 venv.

Nginx is configured
to send EventStream connection requests to
[Pushpin](https://pushpin.org),
and to send all other requests
directly to the Django port.

Pushpin is installed from the project's apt repo,
and it's configured to run on localhost
and route all requests to the Django port.

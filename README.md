# PBX project roles

This repo contains
Ansible roles to install
a PBX service
on the [stack-deploy](https://github.com/tessercat/stack-deploy) stack.

The [pakaa-installer](https://github.com/tessercat/pakaa-installer) repo
includes this repo as a submodule
to simplify automatic configuration
of the stack and PBX service.

## Notes

The target platform
is a Debian-based host.

The Django project runs
as a systemd service
in daphne
bound to a unix socket
in a Python 3 venv.

Nginx is configured to use
[nchan](https://github.com/slact/nchan)
to provide a WebSocket client registration endpoint.

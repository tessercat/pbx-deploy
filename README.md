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

The Django call control project
and the FastAPI WebSocket API application
run as a systemd services
in Python 3 venvs.

# WebRTC peers project roles

This repo contains
Ansible roles to install
a simple WebRTC signaling service
on the [stack-deploy](https://github.com/tessercat/stack-deploy) stack.

The [peers-installer](https://github.com/tessercat/peers-installer) repo
includes this repo as a submodule
to simplify automatic configuration
of the stack and peer service.

## Notes

The target platform
is a Debian-based host.

The Django project runs
as a systemd service
in daphne
bound to a unix socket
in a Python 3 venv.

Nginx is configured
to provide an EventSource client registration endpoint via
[nchan](https://github.com/slact/nchan)
using the
[X-Accel-Redirect](https://github.com/slact/nchan#x-accel-redirect)
technique.

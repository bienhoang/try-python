#!/usr/bin/env bash
set -euo pipefail

redis_port=6379
redis_host=localhost

exec ${redis_socket}<>/dev/tcp/$redis_host/$redis_port

echo 'set somekey 33' >&${redis_socket} # this writes to the filedescriptor $redis_socket
cat <&${redis_socket}
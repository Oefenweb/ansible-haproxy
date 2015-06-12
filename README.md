## haproxy

[![Build Status](https://travis-ci.org/Oefenweb/ansible-haproxy.svg?branch=master)](https://travis-ci.org/Oefenweb/ansible-haproxy) [![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-haproxy-blue.svg)](https://galaxy.ansible.com/list#/roles/3856)

Set up the latest version of [HAProxy](http://www.haproxy.org/) in Ubuntu systems.

#### Requirements

* `python-apt`

#### Variables

* `haproxy_install`: [default: `[]`]: Additional packages to install (e.g. `socat`)

* `haproxy_global_log`: [default: See `defaults/main.yml`]: Log declarations
* `haproxy_global_log.{n}.address`: [required]: Indicates where to send the logs (e.g. `/dev/log`)
* `haproxy_global_log.{n}.facility`: [required]: Must be one of the 24 standard syslog facilities (e.g. `local0`, `local1`)
* `haproxy_global_log.{n}.level`: [optional]: Can be specified to filter outgoing messages (e.g. `notice`)
* `haproxy_global_log.{n}.minlevel`: [optional]: Can be specified to filter outgoing messages (e.g. `notice`)
* `haproxy_global_log.{n}.format`: [optional]: Specifies the log format string to use for traffic logs (e.g. `%{+Q}o\ %t\ %s\ %{-Q}r`)
* `haproxy_global_chroot`: [default: `/var/lib/haproxy`]: Changes current directory to `<jail dir>` and performs a `chroot()` there before dropping privileges
* `haproxy_global_stats`: [default: See `defaults/main.yml`]: Stats declarations
* `haproxy_global_stats.socket`:  [default: `"{{ '/run/haproxy/admin.sock' if ansible_distribution_version | version_compare('12.04', '>=') else '/var/run/haproxy/admin.sock' }}"`]: Binds a UNIX socket to `<path>` or a TCPv4/v6 address to `<address:port>`. Connections to this socket will return various statistics outputs and even allow some commands to be issued to change some runtime settings
* `haproxy_global_stats.timeout`:  [default: `30s`]: The default timeout on the stats socket
* `haproxy_global_user`: [default: `haproxy`]: Similar to `"uid"` but uses the UID of user name `<user name>` from `/etc/passwd`
* `haproxy_global_group`: [default: `haproxy`]: Similar to `"gid"` but uses the GID of group name `<group name>` from `/etc/group`.
* `haproxy_global_daemon`: [default: `true`]: Makes the process fork into background. This is the recommended mode of operation
* `haproxy_global_ca_base`: [default: `/etc/ssl/certs`]: Assigns a default directory to fetch SSL CA certificates and CRLs from when a relative path is used with `"ca-file"` or `"crl-file"` directives
* `haproxy_global_crt_base`: [default: `/etc/ssl/private`]: Assigns a default directory to fetch SSL certificates from when a relative path is used with `"crtfile"` directives
* `haproxy_global_ssl_default_bind_ciphers`: [default: `kEECDH+aRSA+AES:kRSA+AES:+AES256:RC4-SHA:!kEDH:!LOW:!EXP:!MD5:!aNULL:!eNULL`]: This setting is only available when support for OpenSSL was built in. It sets the default string describing the list of cipher algorithms (`"cipher suite"`) that are negotiated during the SSL/TLS handshake for all `"bind"` lines which do not explicitly define theirs
* `haproxy_global_ssl_default_bind_options`: [default: `no-sslv3`]: This setting is only available when support for OpenSSL was built in. It sets default ssl-options to force on all `"bind"` lines

* `haproxy_defaults_log`: [default: `global`]: Enable per-instance logging of events and traffic. `global` should be used when the instance's logging parameters are the same as the global ones. This is the most common usage
* `haproxy_defaults_mode`: [default: `http`]: Set the running mode or protocol of the instance
* `haproxy_defaults_option:  [default: `[httplog, dontlognull]`]:
* `haproxy_defaults_timeout`: [default: See `defaults/main.yml`]: Timeout declarations
* `haproxy_defaults_timeout.type`: [required]: The type (e.g. `connect`, `client`, `server`)
* `haproxy_defaults_timeout.timeout`: [required]: The timeout (in in milliseconds by default, but can be in any other unit if the number is suffixed by the unit) (e.g. `5000`, `50000`)
* `haproxy_defaults_errorfile`: [default: See `defaults/main.yml`]: Errorfile declarations
* `haproxy_defaults_errorfile.code`: [required]: The HTTP status code. Currently, HAProxy is capable of generating codes 200, 400, 403, 408, 500, 502, 503, and 504 (e.g. `400`)
* `haproxy_defaults_errorfile.file`: [required]: A file containing the full HTTP response (e.g `/etc/haproxy/errors/400.http`)

* `haproxy_ssl_map`: [default: `[]`]: SSL declarations
* `haproxy_ssl_map.{n}.src`: The local path of the file to copy, can be absolute or relative (e.g. `../../../files/haproxy/etc/haproxy/ssl/star-example-com.pem`)
* `haproxy_ssl_map.{n}.dest`: The remote path of the file to copy (e.g. `/etc/haproxy/ssl/star-example-com.pem`)
* `haproxy_ssl_map.{n}.owner`: The name of the user that should own the file (optional, default `root`)
* `haproxy_ssl_map.{n}.group`: The name of the group that should own the file (optional, default `root`)
* `haproxy_ssl_map.{n}.mode`: The mode of the file, such as 0644 (optional, default `0640`)

* `haproxy_listen`: [default: `[]`]: Listen declarations

* `haproxy_frontend`: [default: `[]`]: Front-end declarations

* `haproxy_backend`: [default: `[]`]: Back-end declarations

## Dependencies

None

#### SSL Termination (Multiple certificates, global monitoring, multiple web servers)

```yaml
---
- hosts: all
  roles:
  - haproxy
  vars:
    haproxy_ssl_map:
      - src: ../../../files/haproxy/etc/haproxy/ssl/star-example0-com.pem
        dest: /etc/ssl/private/star-example0-com.pem
      - src: ../../../files/haproxy/etc/haproxy/ssl/star-example1-com.pem
        dest: /etc/ssl/private/star-example1-com.pem
      - src: ../../../files/haproxy/etc/haproxy/ssl/star-example2-com.pem
        dest: /etc/ssl/private/star-example2-com.pem

    haproxy_listen:
      - name: stats
        description: Global statistics
        bind: '0.0.0.0:1936'
        mode: http
        stats:
          enable: true
          uri: /
          hide_version: true
          refresh: 5s
          auth:
            - user: admin
              passwd: 'NqXgKWQ9f9Et'
        ssl:
          - crt: star-example0-com.pem

    haproxy_frontend:
      - name: http
        description: Front-end for all HTTP traffic
        bind: '0.0.0.0:80'
        mode: http
        default_backend: webservers
      - name: https
        description: Front-end for all HTTPS traffic
        bind: '0.0.0.0:443'
        ssl:
          - crt: star-example1-com.pem
          - crt: star-example2-com.pem
        mode: http
        default_backend: webservers
        rspadd:
          - string: 'Strict-Transport-Security:\ max-age=15768000'

    haproxy_backend:
      - name: webservers
        description: Back-end with all (Apache) webservers
        mode: http
        balance: roundrobin
        option:
          - forwardfor
          - 'httpchk HEAD / HTTP/1.1\r\nHost:localhost'
        http_request:
          - action: 'set-header'
            param: 'X-Forwarded-Port %[dst_port]'
          - action: 'add-header'
            param: 'X-Forwarded-Proto https'
            cond: 'if { ssl_fc }'
        server:
          - name: web01
            ip: 127.0.0.1
            port: 8001
            maxconn: 501
            params:
              - check
          - name: web02
            ip: 127.0.0.1
            port: 8002
            maxconn: 502
            params:
              - check
          - name: web03
            ip: 127.0.0.1
            port: 8003
            maxconn: 503
```

#### License

MIT

#### Author Information

Mischa ter Smitten (based on work of [FloeDesignTechnologies](https://github.com/FloeDesignTechnologies))

#### Feedback, bug-reports, requests, ...

Are [welcome](https://github.com/Oefenweb/ansible-haproxy/issues)!

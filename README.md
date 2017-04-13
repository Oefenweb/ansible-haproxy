## haproxy

[![Build Status](https://travis-ci.org/Oefenweb/ansible-haproxy.svg?branch=master)](https://travis-ci.org/Oefenweb/ansible-haproxy) [![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-haproxy-blue.svg)](https://galaxy.ansible.com/tersmitten/haproxy)

Set up (the latest version of) [HAProxy](http://www.haproxy.org/) in Ubuntu systems.

#### Requirements

* `python-apt`

#### Variables

* `haproxy_version`: [default: `1.6`]: Version to install (e.g. `1.5`, `1.6`, `1.7`)

* `haproxy_install`: [default: `[]`]: Additional packages to install (e.g. `socat`)

* `haproxy_global_log`: [default: See `defaults/main.yml`]: Log declarations
* `haproxy_global_log.{n}.address`: [required]: Indicates where to send the logs (e.g. `/dev/log`)
* `haproxy_global_log.{n}.facility`: [required]: Must be one of the 24 standard syslog facilities (e.g. `local0`, `local1`)
* `haproxy_global_log.{n}.level`: [optional]: Can be specified to filter outgoing messages (e.g. `notice`)
* `haproxy_global_log.{n}.minlevel`: [optional]: Can be specified to filter outgoing messages (e.g. `notice`)
* `haproxy_global_log.{n}.format`: [optional]: Specifies the log format string to use for traffic logs (e.g. `%{+Q}o\ %t\ %s\ %{-Q}r`)
* `haproxy_global_chroot`: [default: `/var/lib/haproxy`]: Changes current directory to `<jail dir>` and performs a `chroot()` there before dropping privileges
* `haproxy_global_stats`: [default: See `defaults/main.yml`]: Stats declarations
* `haproxy_global_stats.sockets`:  [default: `[{listen: /run/haproxy/admin.sock }}"}]`]: Sockets declarations
* `haproxy_global_stats.sockets.{n}.listen`:  [required]: Defines a listening address and/or ports (e.g. `/run/haproxy/admin.sock`)
* `haproxy_global_stats.sockets.{n}.param`:  [optional]: A list of parameters common to this bind declarations (e.g. `['mode 660', 'level admin', 'process 1']`)
* `haproxy_global_stats.timeout`:  [optional]: The default timeout on the stats socket
* `haproxy_global_user`: [default: `haproxy`]: Similar to `"uid"` but uses the UID of user name `<user name>` from `/etc/passwd`
* `haproxy_global_group`: [default: `haproxy`]: Similar to `"gid"` but uses the GID of group name `<group name>` from `/etc/group`.
* `haproxy_global_daemon`: [default: `true`]: Makes the process fork into background. This is the recommended mode of operation
* `haproxy_global_maxconn`: [optional]: Sets the maximum per-process number of concurrent connections
* `haproxy_global_ca_base`: [default: `/etc/ssl/certs`]: Assigns a default directory to fetch SSL CA certificates and CRLs from when a relative path is used with `"ca-file"` or `"crl-file"` directives
* `haproxy_global_crt_base`: [default: `/etc/ssl/private`]: Assigns a default directory to fetch SSL certificates from when a relative path is used with `"crtfile"` directives
* `haproxy_global_ssl_default_bind_ciphers`: [default: `kEECDH+aRSA+AES:kRSA+AES:+AES256:RC4-SHA:!kEDH:!LOW:!EXP:!MD5:!aNULL:!eNULL`]: This setting is only available when support for OpenSSL was built in. It sets the default string describing the list of cipher algorithms ("cipher suite") that are negotiated during the SSL/TLS handshake for all `"bind"` lines which do not explicitly define theirs
* `haproxy_global_ssl_default_bind_options`: [default: `no-sslv3`]: This setting is only available when support for OpenSSL was built in. It sets default ssl-options to force on all `"bind"` lines
* `haproxy_global_ssl_default_server_ciphers`: [default: `kEECDH+aRSA+AES:kRSA+AES:+AES256:RC4-SHA:!kEDH:!LOW:!EXP:!MD5:!aNULL:!eNULL`]: This setting is only available when support for OpenSSL was built in. It sets the default string describing the list of cipher algorithms that are negotiated during the SSL/TLS handshake with the server, for all `"server"` lines which do not explicitly define theirs
* `haproxy_global_ssl_default_server_options`: [default: `no-sslv3`]: This setting is only available when support for OpenSSL was built in. It sets default ssl-options to force on all `"server"` lines
* `haproxy_global_nbproc`: [default: `1`]: Number of processes to create when going daemon. This requires the `daemon` mode. By default, only one process is created, which is the recommended mode of operation
* `haproxy_global_tune`: [default: `[]`]: (Performance) tuning declarations
* `haproxy_global_tune.{n}.key`: [required]: Setting name (e.g. `ssl.cachesize`)
* `haproxy_global_tune.{n}.value`: [required]: Setting value (e.g. `50000`)
* `haproxy_global_option:  [default: `[]`]: Options (global)

* `haproxy_defaults_log`: [default: `global`]: Enable per-instance logging of events and traffic. `global` should be used when the instance's logging parameters are the same as the global ones. This is the most common usage
* `haproxy_defaults_mode`: [default: `http`]: Set the running mode or protocol of the instance
* `haproxy_defaults_source`: [optional]: Set the source address or interface for connections from the proxy
* `haproxy_defaults_option`: [default: `[httplog, dontlognull]`]: Options (default)
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
* `haproxy_listen.{n}.name`: [required]: The name of the section (e.g. `stats`)
* `haproxy_listen.{n}.description`: [optional]: A description of the section (e.g. `Global statistics`)
* `haproxy_listen.{n}.bind`: [required]: Bind declarations
* `haproxy_listen.{n}.bind.{n}.listen`: [required]: Defines one or several listening addresses and/or ports (e.g. `0.0.0.0:1936`)
* `haproxy_listen.{n}.bind.{n}.param`: [optional]: A list of parameters common to this bind declarations
* `haproxy_listen.{n}.bind_process`:  [optional]: Limits the declaration to a certain set of processes numbers (e.g. `[all]`, `[1]`, `[2 ,3, 4]`)
* `haproxy_listen.{n}.mode`: [required]: Set the running mode or protocol of the section (e.g. `http`)
* `haproxy_listen.{n}.balance`: [required]: The load balancing algorithm to be used (e.g. `roundrobin`)
* `haproxy_listen.{n}.maxconn`: [optional]: Fix the maximum number of concurrent connections
* `haproxy_listen.{n}.source`: [optional]: Set the source address or interface for connections from the proxy
* `haproxy_listen.{n}.option`: [optional]: Options to set (e.g. `[dontlog-normal]`)
* `haproxy_listen.{n}.no_option`: [optional]: Options to set (e.g. `[dontlog-normal]`)
* `haproxy_listen.{n}.tcp_check`: [optional]: Perform health checks using tcp-check send/expect sequences (e.g. `['expect string +OK\ POP3\ ready']`)
* `haproxy_listen.{n}.timeout`: [optional]: Timeout declarations
* `haproxy_listen.{n}.timeout.type`: [required]: The type (e.g. `connect`, `client`, `server`)
* `haproxy_listen.{n}.timeout.timeout`: [required]: The timeout (in in milliseconds by default, but can be in any other unit if the number is suffixed by the unit) (e.g. `5000`, `50000`)
* `haproxy_listen.{n}.capture`: [optional]: Capture fields from request or response
* `haproxy_listen.{n}.capture.type`: [required]: What to capture (`cookie`, `request header`, `response header`)
* `haproxy_listen.{n}.capture.name`: [required]: Name of the header or cookie to capture
* `haproxy_listen.{n}.capture.length`: [required]: Maximum number of characters to capture and report in the logs
* `haproxy_listen.{n}.http_request`: [optional]: Access control for Layer 7 requests
* `haproxy_listen.{n}.http_request.{n}.action`: [required]: The rules action (e.g. `add-header`)
* `haproxy_listen.{n}.http_request.{n}.param`: [optional]: The complete line to be added (e.g. `X-Forwarded-Proto https`)
* `haproxy_listen.{n}.http_request.{n}.cond`: [optional]: A matching condition built from ACLs (e.g. `if { ssl_fc }`)
* `haproxy_listen.{n}.http_response`: [optional]: Access control for Layer 7 responses
* `haproxy_listen.{n}.http_response.{n}.action`: [required]: The rules action (e.g. `del-header`)
* `haproxy_listen.{n}.http_response.{n}.param`: [optional]: The complete line to be added (e.g. `X-Varnish`)
* `haproxy_listen.{n}.http_response.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_listen.{n}.stats`: [optional]: Stats declarations
* `haproxy_listen.{n}.stats.enable`: [required]: Enables statistics reporting with default settings
* `haproxy_listen.{n}.stats.uri`: [optional, default `/`]: Define the URI prefix to access statistics
* `haproxy_listen.{n}.stats.options`: [optional]: List of boolean stats options (e.g. `hide-version`, `show-node`, `show-desc`, `show-legends`)
* `haproxy_listen.{n}.stats.refresh`: [optional]: Defined the refresh delay, specified in seconds (e.g. `5s`)
* `haproxy_listen.{n}.stats.admin`: [optional]: Define / enable admin part of web interface with conditional attached
* `haproxy_listen.{n}.stats.auth`: [optional]: Auth declarations
* `haproxy_listen.{n}.stats.auth.{n}.user`: [required]: A user name to grant access to
* `haproxy_listen.{n}.stats.auth.{n}.passwd`: [required]: The cleartext password associated to this user
* `haproxy_listen.{n}.server`: [optional]: Server declarations
* `haproxy_listen.{n}.server.{n}.name`: [required]: The internal name assigned to this server
* `haproxy_listen.{n}.server.{n}.listen`: [required]: Defines a listening address and/or ports
* `haproxy_listen.{n}.server.{n}.param`: [optional]: A list of parameters for this server
* `haproxy_listen.{n}.rspadd`: [optional]: Adds headers at the end of the HTTP response
* `haproxy_listen.{n}.rspadd.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_listen.{n}.rspadd.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_listen.{n}.redirect`: [optional]: Return an HTTP redirection if/unless a condition is matched
* `haproxy_listen.{n}.redirect.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_listen.{n}.redirect.{n}.cond`: [optional]: A condition to apply this rule
* `haproxy_listen.{n}.acl`: [optional]: Create an ACL check which can be later used in evaluations/conditionals
* `haproxy_listen.{n}.acl.{n}.string`: [required]: ACL entry to be used in conditional check later
* `haproxy_listen.{n}.rsprep`: [optional]: Response regexp edit definition
* `haproxy_listen.{n}.rsprep.{n}.string`: [required]: Regexp definition to be used on response
* `haproxy_listen.{n}.rsprep.{n}.cond`: [optional]: A condition to apply this rule

* `haproxy_frontend`: [default: `[]`]: Front-end declarations
* `haproxy_frontend.{n}.name`: [required]: The name of the section (e.g. `https`)
* `haproxy_frontend.{n}.description`: [optional]: A description of the section (e.g. `Front-end for all HTTPS traffic`)
* `haproxy_frontend.{n}.bind`: [required]: Bind declarations
* `haproxy_frontend.{n}.bind.{n}.listen`: [required]: Defines one or several listening addresses and/or ports (e.g. `0.0.0.0:443`)
* `haproxy_frontend.{n}.bind.{n}.param`: [optional]: A list of parameters common to this bind declarations
* `haproxy_frontend.{n}.bind_process`:  [optional]: Limits the declaration to a certain set of processes numbers (e.g. `[all]`, `[1]`, `[2 ,3, 4]`)
* `haproxy_frontend.{n}.mode`: [required]: Set the running mode or protocol of the section (e.g. `http`)
* `haproxy_frontend.{n}.maxconn`: [optional]: Fix the maximum number of concurrent connections
* `haproxy_frontend.{n}.option`: [optional]: Options to set (e.g. `[tcplog]`)
* `haproxy_frontend.{n}.no_option`: [optional]: Options to unset (e.g. `[forceclose]`)
* `haproxy_frontend.{n}.timeout`: [optional]: Timeout declarations
* `haproxy_frontend.{n}.timeout.type`: [required]: The type (e.g. `client`)
* `haproxy_frontend.{n}.timeout.timeout`: [required]: The timeout (in in milliseconds by default, but can be in any other unit if the number is suffixed by the unit) (e.g. `5000`, `50000`)
* `haproxy_frontend.{n}.capture`: [optional]: Capture fields from request or response
* `haproxy_frontend.{n}.capture.type`: [required]: What to capture (`cookie`, `request header`, `response header`)
* `haproxy_frontend.{n}.capture.name`: [required]: Name of the header or cookie to capture
* `haproxy_frontend.{n}.capture.length`: [required]: Maximum number of characters to capture and report in the logs
* `haproxy_frontend.{n}.http_request`: [optional]: Access control for Layer 7 requests
* `haproxy_frontend.{n}.http_request.{n}.action`: [required]: The rules action (e.g. `add-header`)
* `haproxy_frontend.{n}.http_request.{n}.param`: [optional]: The complete line to be added (e.g. `X-Forwarded-Proto https`)
* `haproxy_frontend.{n}.http_request.{n}.cond`: [optional]: A matching condition built from ACLs (e.g. `if { ssl_fc }`)
* `haproxy_frontend.{n}.http_response`: [optional]: Access control for Layer 7 responses
* `haproxy_frontend.{n}.http_response.{n}.action`: [required]: The rules action (e.g. `del-header`)
* `haproxy_frontend.{n}.http_response.{n}.param`: [optional]: The complete line to be added (e.g. `X-Varnish`)
* `haproxy_frontend.{n}.http_response.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_frontend.{n}.use_backend`: [optional]: Switch to a specific backend if/unless a Layer 7 condition is matched. (e.g. '%[req.hdr(host),lower,map_dom(/etc/haproxy/haproxy_backend.map,bk_default)]' or `['foo-backend if is_foo', 'bar-backend if is_bar']`)
* `haproxy_frontend.{n}.default_backend`: [required]: The backend to use when no `"use_backend"` rule has been matched (e.g. `webservers`)
* `haproxy_frontend.{n}.rspadd`: [optional]: Adds headers at the end of the HTTP response
* `haproxy_frontend.{n}.rspadd.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_frontend.{n}.rspadd.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_frontend.{n}.redirect`: [optional]: Return an HTTP redirection if/unless a condition is matched
* `haproxy_frontend.{n}.redirect.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_frontend.{n}.redirect.{n}.cond`: [optional]: A condition to apply this rule
* `haproxy_frontend.{n}.acl`: [optional]: Create an ACL check which can be later used in evaluations/conditionals
* `haproxy_frontend.{n}.acl.{n}.string`: [required]: ACL entry to be used in conditional check later
* `haproxy_frontend.{n}.rsprep`: [optional]: Response regexp edit definition
* `haproxy_frontend.{n}.rsprep.{n}.string`: [required]: Regexp definition to be used on response
* `haproxy_frontend.{n}.rsprep.{n}.cond`: [optional]: A condition to apply this rule

* `haproxy_backend`: [default: `[]`]: Back-end declarations
* `haproxy_backend.{n}.name`: [required]: The name of the section (e.g. `webservers`)
* `haproxy_backend.{n}.description`: [optional]: A description of the section (e.g. `Back-end with all (Apache) webservers`)
* `haproxy_backend.{n}.bind_process`:  [optional]: Limits the declaration to a certain set of processes numbers (e.g. `[all]`, `[1]`, `[2 ,3, 4]`)
* `haproxy_backend.{n}.mode`: [required]: Set the running mode or protocol of the section (e.g. `http`)
* `haproxy_backend.{n}.balance`: [required]: The load balancing algorithm to be used (e.g. `roundrobin`)
* `haproxy_backend.{n}.source`: [optional]: Set the source address or interface for connections from the proxy
* `haproxy_backend.{n}.option`: [optional]: Options to set (e.g. `[forwardfor]`)
* `haproxy_backend.{n}.no_option`: [optional]: Options to unset (e.g. `[forceclose]`)
* `haproxy_backend.{n}.tcp_check`: [optional]: Perform health checks using tcp-check send/expect sequences (e.g. `['expect string +OK\ POP3\ ready']`)
* `haproxy_backend.{n}.timeout`: [optional]: Timeout declarations
* `haproxy_backend.{n}.timeout.type`: [required]: The type (e.g. `server`)
* `haproxy_backend.{n}.timeout.timeout`: [required]: The timeout (in in milliseconds by default, but can be in any other unit if the number is suffixed by the unit) (e.g. `5000`, `50000`)
* `haproxy_backend.{n}.http_request`: [optional]: Access control for Layer 7 requests
* `haproxy_backend.{n}.http_request.{n}.action`: [required]: The rules action (e.g. `add-header`)
* `haproxy_backend.{n}.http_request.{n}.param`: [optional]: The complete line to be added (e.g. `X-Forwarded-Proto https`)
* `haproxy_backend.{n}.http_request.{n}.cond`: [optional]: A matching condition built from ACLs (e.g. `if { ssl_fc }`)
* `haproxy_backend.{n}.http_response`: [optional]: Access control for Layer 7 responses
* `haproxy_backend.{n}.http_response.{n}.action`: [required]: The rules action (e.g. `del-header`)
* `haproxy_backend.{n}.http_response.{n}.param`: [optional]: The complete line to be added (e.g. `X-Varnish`)
* `haproxy_backend.{n}.http_response.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_backend.{n}.server`: [optional]: Server declarations
* `haproxy_backend.{n}.server.{n}.name`: [required]: The internal name assigned to this server
* `haproxy_backend.{n}.server.{n}.listen`: [required]: Defines a listening address and/or ports
* `haproxy_backend.{n}.server.{n}.param`: [optional]: A list of parameters for this server

## Dependencies

None

#### SSL Termination 1

* **Single core**
* Multiple certificates (SNI)
* Global monitoring
* Multiple web servers

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
        bind:
          - listen: '0.0.0.0:1936'
            param:
              - ssl
              - 'crt star-example0-com.pem'
        mode: http
        stats:
          enable: true
          uri: /
          options:
            - hide-version
            - show-node
          admin: if LOCALHOST
          refresh: 5s
          auth:
            - user: admin
              passwd: 'NqXgKWQ9f9Et'

    haproxy_frontend:
      - name: http
        description: Front-end for all HTTP traffic
        bind:
          - listen: "{{ ansible_eth0['ipv4']['address'] }}:80"
        mode: http
        redirect:
          - string: 'scheme https code 301'
            cond: 'if !{ ssl_fc }'
        default_backend: webservers
      - name: https
        description: Front-end for all HTTPS traffic
        bind:
          - listen: "{{ ansible_eth0['ipv4']['address'] }}:443"
            param:
              - ssl
              - 'crt star-example1-com.pem'
              - 'crt star-example2-com.pem'
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
          - name: web-01
            listen: "{{ ansible_lo['ipv4']['address'] }}:8001"
            param:
              - 'maxconn 501'
              - check
          - name: web-02
            listen: "{{ ansible_lo['ipv4']['address'] }}:8002"
            param:
              - 'maxconn 502'
              - check
          - name: web-03
            listen: "{{ ansible_lo['ipv4']['address'] }}:8003"
            param:
              - 'maxconn 503'
              - check
```

#### SSL Termination 2

* **Multi core**
  * [How Stack Exchange gets the most out of HAProxy](http://brokenhaze.com/blog/2014/03/25/how-stack-exchange-gets-the-most-out-of-haproxy/)
  * [HAproxy: mapping process to CPU core for maximum performance](http://blog.onefellow.com/post/82478335338/haproxy-mapping-process-to-cpu-core-for-maximum)
* Multiple certificates (SNI)
* Global monitoring
* Multiple web servers

```yaml
- hosts: all
  roles:
    - haproxy
  vars:
    haproxy_global_stats_sockets_default_param:
      - 'mode 660'
      - 'level admin'
    haproxy_global_stats:
      sockets:
        - listen: /run/haproxy/admin-1.sock
          param: "{{ haproxy_global_stats_sockets_default_param + ['process 1'] }}"
        - listen: /run/haproxy/admin-2.sock
          param: "{{ haproxy_global_stats_sockets_default_param + ['process 2'] }}"
        - listen: /run/haproxy/admin-3.sock
          param: "{{ haproxy_global_stats_sockets_default_param + ['process 3'] }}"
        - listen: /run/haproxy/admin-4.sock
          param: "{{ haproxy_global_stats_sockets_default_param + ['process 4'] }}"
      timeout: 30s

    haproxy_global_nbproc: 4

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
        bind:
          - listen: "{{ ansible_eth0['ipv4']['address'] }}:1936"
            param:
              - ssl
              - 'crt star-example0-com.pem'
        bind_process:
          - 1
        mode: http
        stats:
          enable: true
          uri: /
          options:
            - hide-version
            - show-desc
          refresh: 5s
          admin: if TRUE
          auth:
            - user: admin
              passwd: 'NqXgKWQ9f9Et'
      - name: ssl-proxy
        description: Proxy for all HTTPS traffic
        bind:
          - listen: "{{ ansible_eth0['ipv4']['address'] }}:443"
            param:
              - ssl
              - 'crt star-example1-com.pem'
              - 'crt star-example2-com.pem'
        bind_process:
          - 2
          - 3
          - 4
        acl:
          - string: secure dst_port eq 443
        mode: http
        server:
          - name: "{{ inventory_hostname }}"
            listen: "{{ ansible_lo['ipv4']['address'] }}:80"
            param:
              - send-proxy
        rspadd:
          - string: 'Strict-Transport-Security:\ max-age=15768000'
        rsprep:
          - string: '^Set-Cookie:\ (.*) Set-Cookie:\ \1;\ Secure'
            cond: if secure

    haproxy_frontend:
      - name: http
        description: Front-end for all HTTP traffic
        bind:
          - listen: "{{ ansible_eth0['ipv4']['address'] }}:80"
          - listen: "{{ ansible_lo['ipv4']['address'] }}:80"
            param:
              - accept-proxy
        bind_process:
          - 1
        mode: http
        default_backend: webservers

    haproxy_backend:
      - name: webservers
        description: Back-end with all (Apache) webservers
        bind_process:
          - 1
        mode: http
        balance: roundrobin
        option:
          - forwardfor
          - 'httpchk HEAD / HTTP/1.1\r\nHost:\ localhost'
        http_request:
          - action: 'set-header'
            param: 'X-Forwarded-Port %[dst_port]'
          - action: 'add-header'
            param: 'X-Forwarded-Proto https'
            cond: 'if { dst_port 443 }'
        server:
          - name: web-01
            listen: "{{ ansible_lo['ipv4']['address'] }}:8001"
            param:
              - 'maxconn 501'
              - check
          - name: web-02
            listen: "{{ ansible_lo['ipv4']['address'] }}:8002"
            param:
              - 'maxconn 502'
              - check
          - name: web-03
            listen: "{{ ansible_lo['ipv4']['address'] }}:8003"
            param:
              - 'maxconn 503'
              - check
```

#### Memcached (frontend / backend)

```yaml
---
- hosts: all
  roles:
    - haproxy
  vars:
    haproxy_frontend:
      - name: memcached
        bind:
          - listen: '127.0.0.1:11211'
        mode: tcp
        option:
          - dontlog-normal
        default_backend: memcached-servers

    haproxy_backend:
      - name: memcached-servers
        mode: tcp
        option:
          - dontlog-normal
        balance: roundrobin
        server:
          - name: memcached-01
            listen: '127.0.1.1:11211'
            param:
              - check
          - name: memcached-02
            listen: '127.0.2.1:11211'
            param:
              - check
              - backup
```

#### Redis (listen)

```yaml
---
- hosts: all
  roles:
    - haproxy
  vars:
    haproxy_listen:
      - name: redis
        description: Redis servers
        bind:
          - listen: '127.0.0.1:6379'
        mode: tcp
        option:
          - dontlog-normal
          - tcplog
          - tcp-check
        tcp_check:
          - 'send PING\r\n'
          - 'expect string +PONG'
          - 'send QUIT\r\n'
          - 'expect string +OK'
        balance: roundrobin
        server:
          - name: redis-01
            listen: '127.0.1.1:6379'
            param:
              - check
          - name: redis-02
            listen: '127.0.2.1:6379'
            param:
              - check
              - backup
```

#### License

MIT

#### Author Information

Mischa ter Smitten (based on work of [FloeDesignTechnologies](https://github.com/FloeDesignTechnologies))

#### Feedback, bug-reports, requests, ...

Are [welcome](https://github.com/Oefenweb/ansible-haproxy/issues)!

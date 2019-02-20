## haproxy

[![Build Status](https://travis-ci.org/Oefenweb/ansible-haproxy.svg?branch=master)](https://travis-ci.org/Oefenweb/ansible-haproxy) [![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-haproxy-blue.svg)](https://galaxy.ansible.com/Oefenweb/haproxy)

Set up (the latest version of) [HAProxy](http://www.haproxy.org/) in Ubuntu systems.

#### Requirements

* `python-apt`

#### Variables

* `haproxy_version`: [default: `1.8`]: Version to install (e.g. `1.5`, `1.6`, `1.7`, `1.8`)

* `haproxy_install`: [default: `[]`]: Additional packages to install (e.g. `socat`)

* `haproxy_global_log`: [default: See `defaults/main.yml`]: Log declarations
* `haproxy_global_log.{n}.address`: [required]: Indicates where to send the logs (e.g. `/dev/log`)
* `haproxy_global_log.{n}.facility`: [required]: Must be one of the 24 standard syslog facilities (e.g. `local0`, `local1`)
* `haproxy_global_log.{n}.level`: [optional]: Can be specified to filter outgoing messages (e.g. `notice`)
* `haproxy_global_log.{n}.minlevel`: [optional]: Can be specified to filter outgoing messages (e.g. `notice`)
* `haproxy_global_log.{n}.length`: [optional]: Can be specified to adjust message length in log (e.g. `2048`)
* `haproxy_global_chroot`: [optional]: Changes current directory to `<jail dir>` and performs a `chroot()` there before dropping privileges
* `haproxy_global_stats`: [default: See `defaults/main.yml`]: Stats declarations
* `haproxy_global_stats.sockets`:  [default: `[{listen: /run/haproxy/admin.sock }}"}]`]: Sockets declarations
* `haproxy_global_stats.sockets.{n}.listen`:  [required]: Defines a listening address and/or ports (e.g. `/run/haproxy/admin.sock`)
* `haproxy_global_stats.sockets.{n}.param`:  [optional]: A list of parameters common to this bind declarations (e.g. `['mode 660', 'level admin', 'process 1']`)
* `haproxy_global_stats.timeout`:  [optional]: The default timeout on the stats socket
* `haproxy_global_user`: [default: `haproxy`]: Similar to `"uid"` but uses the UID of user name `<user name>` from `/etc/passwd`
* `haproxy_global_group`: [default: `haproxy`]: Similar to `"gid"` but uses the GID of group name `<group name>` from `/etc/group`.
* `haproxy_global_daemon`: [default: `true`]: Makes the process fork into background. This is the recommended mode of operation
* `haproxy_global_master_worker`: [optional, default: `false`]: Whether or not to use master/worker mode (`>= 1.8.0` only)
* `haproxy_global_maxconn`: [optional]: Sets the maximum per-process number of concurrent connections
* `haproxy_global_ca_base`: [default: `/etc/ssl/certs`]: Assigns a default directory to fetch SSL CA certificates and CRLs from when a relative path is used with `"ca-file"` or `"crl-file"` directives
* `haproxy_global_crt_base`: [default: `/etc/ssl/private`]: Assigns a default directory to fetch SSL certificates from when a relative path is used with `"crtfile"` directives
* `haproxy_global_ssl_default_bind_ciphers`: [default: `kEECDH+aRSA+AES:kRSA+AES:+AES256:RC4-SHA:!kEDH:!LOW:!EXP:!MD5:!aNULL:!eNULL`]: This setting is only available when support for OpenSSL was built in. It sets the default string describing the list of cipher algorithms ("cipher suite") that are negotiated during the SSL/TLS handshake for all `"bind"` lines which do not explicitly define theirs
* `haproxy_global_ssl_default_bind_options`: [default: `no-sslv3`]: This setting is only available when support for OpenSSL was built in. It sets default ssl-options to force on all `"bind"` lines
* `haproxy_global_ssl_default_server_ciphers`: [default: `kEECDH+aRSA+AES:kRSA+AES:+AES256:RC4-SHA:!kEDH:!LOW:!EXP:!MD5:!aNULL:!eNULL`]: This setting is only available when support for OpenSSL was built in. It sets the default string describing the list of cipher algorithms that are negotiated during the SSL/TLS handshake with the server, for all `"server"` lines which do not explicitly define theirs
* `haproxy_global_ssl_default_server_options`: [default: `no-sslv3`]: This setting is only available when support for OpenSSL was built in. It sets default ssl-options to force on all `"server"` lines
* `haproxy_global_ssl_engines`: [optional, default `[]`]: OpenSSL engine declarations (`>= 1.8.0` only)
* `haproxy_global_ssl_engines.{n}.name`: [required]: Sets the OpenSSL engine to use (e.g. `rdrand`)
* `haproxy_global_ssl_engines.{n}.algos`: [optional]: Sets the OpenSSL algorithms to use (e.g. `['RSA']`)
* `haproxy_global_ssl_mode_async`: [optional: default `false`]: Enables asynchronous TLS I/O operations if asynchronous capable SSL engines are used (`>= 1.8.0` only)
* `haproxy_global_nbproc`: [default: `1`]: Number of processes to create when going daemon. This requires the `daemon` mode. By default, only one process is created, which is the recommended mode of operation
* `haproxy_global_nbthread`: [optional]: This setting is only available when support for threads was built in. It creates `<number>` threads for each created processes (`>= 1.8.0` only)
* `haproxy_global_tune`: [default: `[]`]: (Performance) tuning declarations
* `haproxy_global_tune.{n}.key`: [required]: Setting name (e.g. `ssl.cachesize`)
* `haproxy_global_tune.{n}.value`: [required]: Setting value (e.g. `50000`)
* `haproxy_global_option`: [default: `[]`]: Options (e.g. ['lua-load /etc/haproxy/acme-http01-webroot.lua', 'ssl-dh-param-file /etc/haproxy/dhparams.pem'])
* `haproxy_global_peers`: Peer list declarations
* `haproxy_global_peers.{n}.name`: Peer list name (e.g. `mypeers`)
* `haproxy_global_peers.{n}.peers`: Peer declarations
* `haproxy_global_peers.{n}.peers.{n}.name`: [required]: Name of the host (recommended to be `hostname`) (e.g. `haproxy1`)
* `haproxy_global_peers.{n}.peers.{n}.listen`: [required]: IP and port for peer to listen/connect to (e.g. `192.168.0.1:1024`)
* `haproxy_global_raw_options`: [default: `[]`]: Additional arbitrary lines to insert in the section

* `haproxy_defaults_log`: [default: `global`]: Enable per-instance logging of events and traffic. `global` should be used when the instance's logging parameters are the same as the global ones. This is the most common usage
* `haproxy_defaults_logformat`: [optional]: Allows you to customize the logs in http mode and tcp mode (e.g. `%{+Q}o\ %t\ %s\ %{-Q}r`)
* `haproxy_defaults_mode`: [default: `http`]: Set the running mode or protocol of the instance
* `haproxy_defaults_source`: [optional]: Set the source address or interface for connections from the proxy
* `haproxy_defaults_option`: [default: `[httplog, dontlognull]`]: Options (default)
* `haproxy_defaults_no_option`: [optional]: Options to unset (e.g. `[redispatch]`)
* `haproxy_defaults_timeout`: [default: See `defaults/main.yml`]: Timeout declarations
* `haproxy_defaults_timeout.type`: [required]: The type (e.g. `connect`, `client`, `server`)
* `haproxy_defaults_timeout.timeout`: [required]: The timeout (in in milliseconds by default, but can be in any other unit if the number is suffixed by the unit) (e.g. `5000`, `50000`)
* `haproxy_defaults_errorfile`: [default: See `defaults/main.yml`]: Errorfile declarations
* `haproxy_defaults_errorfile.code`: [required]: The HTTP status code. Currently, HAProxy is capable of generating codes 200, 400, 403, 408, 500, 502, 503, and 504 (e.g. `400`)
* `haproxy_defaults_errorfile.file`: [required]: A file containing the full HTTP response (e.g `/etc/haproxy/errors/400.http`)
* `haproxy_defaults_compression`: [optional]: Compression declarations
* `haproxy_defaults_compression.{}.name`: [required]: The compression name (e.g. `algo`, `type`, `offload`)
* `haproxy_defaults_compression.{}.value`: [required]: The compression value, (e.g. if name = algo : one of this values `identity`, `gzip`, `deflate`, `raw-deflate` / if name = type : list of mime type separated by space for example `text/html text/plain text/css` / if name = `offload` value is empty)
* `haproxy_default_server_params`: [optional]: Default server backend parameters passed to each backend/listen server.
* `haproxy_default_raw_options`: [default: `[]`]: Additional arbitrary lines to insert in the section

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
* `haproxy_listen.{n}.no_log`: [optional, default `false`]: Used when the logger list must be flushed. For example, if you don't want to inherit from the default logger list
* `haproxy_listen.{n}.tcp_check`: [optional]: Perform health checks using tcp-check send/expect sequences (e.g. `['expect string +OK\ POP3\ ready']`)
* `haproxy_listen.{n}.http_check`: [optional]: Make HTTP health checks consider response contents or specific status codes (e.g. `expect status 403`)
* `haproxy_listen.{n}.stick`: [optional]: Stick declarations
* `haproxy_listen.{n}.stick.{n}.table`: [required]: Configure the stickiness table for the current section (e.g. `type ip size 500k`)
* `haproxy_listen.{n}.stick.{n}.stick_on`: [required]: Define a request pattern to associate a user to a server (e.g. `src`)
* `haproxy_listen.{n}.timeout`: [optional]: Timeout declarations
* `haproxy_listen.{n}.timeout.type`: [required]: The type (e.g. `connect`, `client`, `server`)
* `haproxy_listen.{n}.timeout.timeout`: [required]: The timeout (in in milliseconds by default, but can be in any other unit if the number is suffixed by the unit) (e.g. `5000`, `50000`)
* `haproxy_listen.{n}.acl`: [optional]: Create an ACL check which can be later used in evaluations/conditionals
* `haproxy_listen.{n}.acl.{n}.string`: [required]: ACL entry to be used in conditional check later
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
* `haproxy_listen.{n}.tcp_request_content`: [optional]: Perform an action on a new session depending on a layer 4-7 condition.
* `haproxy_listen.{n}.tcp_request_content.{n}.action`: [required]: The action for the `tcp-request content` rule.
* `haproxy_listen.{n}.tcp_request_content.{n}.cond`: [optional]: A matching condition for the `tcp-request content` rule.
* `haproxy_listen.{n}.tcp_request_connection`: [optional]: Perform an action on an incoming connection depending on a layer 4 condition.
* `haproxy_listen.{n}.tcp_request_connection.{n}.action`: [required]: The action for the `tcp-request connection` rule.
* `haproxy_listen.{n}.tcp_request_connection.{n}.cond`: [optional]: A matching condition for the `tcp-request connection` rule.
* `haproxy_listen.{n}.tcp_request_session`: [optional]: Perform an action on a validated session depending on a layer 5 condition.
* `haproxy_listen.{n}.tcp_request_session.{n}.action`: [required]: The action for the `tcp-request session` rule.
* `haproxy_listen.{n}.tcp_request_session.{n}.cond`: [optional]: A matching condition for the `tcp-request session` rule.
* `haproxy_listen.{n}.tcp_request_inspect_delay`: [optional]: Set the maximum allowed time to wait for data during content inspection.
* `haproxy_listen.{n}.tcp_request_inspect_delay.{n}.timeout`: [required]: The timeout value in millisecond for the `tcp-request inspect-delay` rule.
* `haproxy_listen.{n}.stats`: [optional]: Stats declarations
* `haproxy_listen.{n}.stats.enable`: [required]: Enables statistics reporting with default settings
* `haproxy_listen.{n}.stats.uri`: [optional, default `/`]: Define the URI prefix to access statistics
* `haproxy_listen.{n}.stats.options`: [optional]: List of boolean stats options (e.g. `hide-version`, `show-node`, `show-desc`, `show-legends`)
* `haproxy_listen.{n}.stats.refresh`: [optional]: Defined the refresh delay, specified in seconds (e.g. `5s`)
* `haproxy_listen.{n}.stats.admin`: [optional]: Define / enable admin part of web interface with conditional attached
* `haproxy_listen.{n}.stats.auth`: [optional]: Auth declarations
* `haproxy_listen.{n}.stats.auth.{n}.user`: [required]: A user name to grant access to
* `haproxy_listen.{n}.stats.auth.{n}.passwd`: [required]: The cleartext password associated to this user
* `haproxy_listen.{n}.compression`: [optional]: Compression declarations
* `haproxy_listen.{n}.compression.{n}.name`: [required]: The compression name (e.g. `algo`, `type`, `offload`)
* `haproxy_listen.{n}.compression.{n}.value`: [required]: The compression value, (e.g. if name = algo : one of this values `identity`, `gzip`, `deflate`, `raw-deflate` / if name = type : list of mime type separated by space for example `text/html text/plain text/css` / if name = `offload` value is empty)
* `haproxy_listen.{n}.server`: [optional]: Server declarations
* `haproxy_listen.{n}.server.{n}.name`: [required]: The internal name assigned to this server
* `haproxy_listen.{n}.server.{n}.listen`: [required]: Defines a listening address and/or ports
* `haproxy_listen.{n}.server.{n}.param`: [optional]: A list of parameters for this server
* `haproxy_listen.{n}.reqadd`: [optional]: Adds headers at the end of the HTTP request
* `haproxy_listen.{n}.reqadd.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_listen.{n}.reqadd.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_listen.{n}.rspadd`: [optional]: Adds headers at the end of the HTTP response
* `haproxy_listen.{n}.rspadd.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_listen.{n}.rspadd.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_listen.{n}.reqdel`: [optional]: Delete all headers matching a regular expression in an HTTP request
* `haproxy_listen.{n}.reqdel.{n}.search`: [required]: The regular expression applied to HTTP headers and to the request line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_listen.{n}.reqdel.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_listen.{n}.reqidel`: [optional]: Delete all headers matching a regular expression in an HTTP request (ignore case)
* `haproxy_listen.{n}.reqidel.{n}.search`: [required]: The regular expression applied to HTTP headers and to the request line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_listen.{n}.reqidel.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_listen.{n}.rspdel`: [optional]: Delete all headers matching a regular expression in an HTTP response
* `haproxy_listen.{n}.rspdel.{n}.search`: [required]: The regular expression applied to HTTP headers and to the response line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_listen.{n}.rspdel.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_listen.{n}.rspidel`: [optional]: Delete all headers matching a regular expression in an HTTP response (ignore case)
* `haproxy_listen.{n}.rspidel.{n}.search`: [required]: The regular expression applied to HTTP headers and to the response line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_listen.{n}.rspidel.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_listen.{n}.reqrep`: [optional]: Replace a regular expression with a string in an HTTP request line
* `haproxy_listen.{n}.reqrep.{n}.search`: [required]: The regular expression applied to HTTP headers and to the request line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_listen.{n}.reqrep.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_listen.{n}.reqrep.{n}.cond`: [optional]: Matching condition built from ACLs
* `haproxy_listen.{n}.reqirep`: [optional]: Replace a regular expression with a string in an HTTP request line (ignore case)
* `haproxy_listen.{n}.reqirep.{n}.search`: [required]: The regular expression applied to HTTP headers and to the request line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_listen.{n}.reqirep.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_listen.{n}.reqirep.{n}.cond`: [optional]: Matching condition built from ACLs
* `haproxy_listen.{n}.rsprep`: [optional]: Replace a regular expression with a string in an HTTP response line
* `haproxy_listen.{n}.rsprep.{n}.search`: [required]: The regular expression applied to HTTP headers and to the response line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_listen.{n}.rsprep.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_listen.{n}.rsprep.{n}.cond`: [optional]: Matching condition built from ACLs
* `haproxy_listen.{n}.rspirep`: [optional]: Replace a regular expression with a string in an HTTP response line (ignore case)
* `haproxy_listen.{n}.rspirep.{n}.search`: [required]: The regular expression applied to HTTP headers and to the response line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_listen.{n}.rspirep.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_listen.{n}.rspirep.{n}.cond`: [optional]: Matching condition built from ACLs
* `haproxy_listen.{n}.redirect`: [optional]: Return an HTTP redirection if/unless a condition is matched
* `haproxy_listen.{n}.redirect.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_listen.{n}.redirect.{n}.cond`: [optional]: A condition to apply this rule
* `haproxy_listen.{n}.errorfile`: [optional]: Errorfile declarations
* `haproxy_listen.{n}.errorfile.{n}.code`: [required]: The HTTP status code. Currently, HAProxy is capable of generating codes 200, 400, 403, 408, 500, 502, 503, and 504 (e.g. `400`)
* `haproxy_listen.{n}.errorfile.{n}.file`: [required]: A file containing the full HTTP response (e.g `/etc/haproxy/errors/400.http`)
* `haproxy_listen.{n}.default_server_params`: [optional]: Default server params applied for each server for this particular listen entry.
* `haproxy_listen.{n}.raw_options`: [default: `[]`]: Additional arbitrary lines to insert in the section

* `haproxy_frontend`: [default: `[]`]: Front-end declarations
* `haproxy_frontend.{n}.name`: [required]: The name of the section (e.g. `https`)
* `haproxy_frontend.{n}.description`: [optional]: A description of the section (e.g. `Front-end for all HTTPS traffic`)
* `haproxy_frontend.{n}.bind`: [required]: Bind declarations
* `haproxy_frontend.{n}.bind.{n}.listen`: [required]: Defines one or several listening addresses and/or ports (e.g. `0.0.0.0:443`)
* `haproxy_frontend.{n}.bind.{n}.param`: [optional]: A list of parameters common to this bind declarations
* `haproxy_frontend.{n}.bind_process`:  [optional]: Limits the declaration to a certain set of processes numbers (e.g. `[all]`, `[1]`, `[2 ,3, 4]`)
* `haproxy_frontend.{n}.mode`: [required]: Set the running mode or protocol of the section (e.g. `http`)
* `haproxy_frontend.{n}.maxconn`: [optional]: Fix the maximum number of concurrent connections
* `haproxy_frontend.{n}.logformat`: [optional]: Specifies the log format string to use for traffic logs (e.g. `%{+Q}o\ %t\ %s\ %{-Q}r`)
* `haproxy_frontend.{n}.stick`: [optional]: Stick declarations
* `haproxy_frontend.{n}.stick.{n}.table`: [required]: Configure the stickiness table for the current section (e.g. `type ip size 500k`)
* `haproxy_frontend.{n}.option`: [optional]: Options to set (e.g. `[tcplog]`)
* `haproxy_frontend.{n}.no_option`: [optional]: Options to unset (e.g. `[forceclose]`)
* `haproxy_frontend.{n}.no_log`: [optional, default `false`]: Used when the logger list must be flushed. For example, if you don't want to inherit from the default logger list
* `haproxy_frontend.{n}.timeout`: [optional]: Timeout declarations
* `haproxy_frontend.{n}.timeout.type`: [required]: The type (e.g. `client`)
* `haproxy_frontend.{n}.timeout.timeout`: [required]: The timeout (in in milliseconds by default, but can be in any other unit if the number is suffixed by the unit) (e.g. `5000`, `50000`)
* `haproxy_frontend.{n}.acl`: [optional]: Create an ACL check which can be later used in evaluations/conditionals
* `haproxy_frontend.{n}.acl.{n}.string`: [required]: ACL entry to be used in conditional check later
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
* `haproxy_frontend.{n}.tcp_request_content`: [optional]: Perform an action on a new session depending on a layer 4-7 condition.
* `haproxy_frontend.{n}.tcp_request_content.{n}.action`: [required]: The action for the `tcp-request content` rule.
* `haproxy_frontend.{n}.tcp_request_content.{n}.cond`: [optional]: A matching condition for the `tcp-request content` rule.
* `haproxy_frontend.{n}.tcp_request_connection`: [optional]: Perform an action on an incoming connection depending on a layer 4 condition.
* `haproxy_frontend.{n}.tcp_request_connection.{n}.action`: [required]: The action for the `tcp-request connection` rule.
* `haproxy_frontend.{n}.tcp_request_connection.{n}.cond`: [optional]: A matching condition for the `tcp-request connection` rule.
* `haproxy_frontend.{n}.tcp_request_session`: [optional]: Perform an action on a validated session depending on a layer 5 condition.
* `haproxy_frontend.{n}.tcp_request_session.{n}.action`: [required]: The action for the `tcp-request session` rule.
* `haproxy_frontend.{n}.tcp_request_session.{n}.cond`: [optional]: A matching condition for the `tcp-request session` rule.
* `haproxy_frontend.{n}.tcp_request_inspect_delay`: [optional]: Set the maximum allowed time to wait for data during content inspection.
* `haproxy_frontend.{n}.tcp_request_inspect_delay.{n}.timeout`: [required]: The timeout value in millisecond for the `tcp-request inspect-delay` rule.
* `haproxy_frontend.{n}.use_backend`: [optional]: Switch to a specific backend if/unless a Layer 7 condition is matched. (e.g. '%[req.hdr(host),lower,map_dom(/etc/haproxy/haproxy_backend.map,bk_default)]' or `['foo-backend if is_foo', 'bar-backend if is_bar']`)
* `haproxy_frontend.{n}.default_backend`: [optional]: The backend to use when no `"use_backend"` rule has been matched (e.g. `webservers`)
* `haproxy_frontend.{n}.reqadd`: [optional]: Adds headers at the end of the HTTP request
* `haproxy_frontend.{n}.reqadd.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_frontend.{n}.reqadd.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_frontend.{n}.rspadd`: [optional]: Adds headers at the end of the HTTP response
* `haproxy_frontend.{n}.rspadd.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_frontend.{n}.rspadd.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_frontend.{n}.reqdel`: [optional]: Delete all headers matching a regular expression in an HTTP request
* `haproxy_frontend.{n}.reqdel.{n}.search`: [required]: The regular expression applied to HTTP headers and to the request line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_frontend.{n}.reqdel.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_frontend.{n}.reqidel`: [optional]: Delete all headers matching a regular expression in an HTTP request (ignore case)
* `haproxy_frontend.{n}.reqidel.{n}.search`: [required]: The regular expression applied to HTTP headers and to the request line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_frontend.{n}.reqidel.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_frontend.{n}.rspdel`: [optional]: Delete all headers matching a regular expression in an HTTP response
* `haproxy_frontend.{n}.rspdel.{n}.search`: [required]: The regular expression applied to HTTP headers and to the response line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_frontend.{n}.rspdel.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_frontend.{n}.rspidel`: [optional]: Delete all headers matching a regular expression in an HTTP response (ignore case)
* `haproxy_frontend.{n}.rspidel.{n}.search`: [required]: The regular expression applied to HTTP headers and to the response line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_frontend.{n}.rspidel.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_frontend.{n}.reqrep`: [optional]: Replace a regular expression with a string in an HTTP request line
* `haproxy_frontend.{n}.reqrep.{n}.search`: [required]: The regular expression applied to HTTP headers and to the request line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_frontend.{n}.reqrep.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_frontend.{n}.reqrep.{n}.cond`: [optional]: Matching condition built from ACLs
* `haproxy_frontend.{n}.reqirep`: [optional]: Replace a regular expression with a string in an HTTP request line (ignore case)
* `haproxy_frontend.{n}.reqirep.{n}.search`: [required]: The regular expression applied to HTTP headers and to the request line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_frontend.{n}.reqirep.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_frontend.{n}.reqirep.{n}.cond`: [optional]: Matching condition built from ACLs
* `haproxy_frontend.{n}.rsprep`: [optional]: Replace a regular expression with a string in an HTTP response line
* `haproxy_frontend.{n}.rsprep.{n}.search`: [required]: The regular expression applied to HTTP headers and to the response line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_frontend.{n}.rsprep.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_frontend.{n}.rsprep.{n}.cond`: [optional]: Matching condition built from ACLs
* `haproxy_frontend.{n}.rspirep`: [optional]: Replace a regular expression with a string in an HTTP response line (ignore case)
* `haproxy_frontend.{n}.rspirep.{n}.search`: [required]: The regular expression applied to HTTP headers and to the response line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_frontend.{n}.rspirep.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_frontend.{n}.rspirep.{n}.cond`: [optional]: Matching condition built from ACLs
* `haproxy_frontend.{n}.redirect`: [optional]: Return an HTTP redirection if/unless a condition is matched
* `haproxy_frontend.{n}.redirect.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_frontend.{n}.redirect.{n}.cond`: [optional]: A condition to apply this rule
* `haproxy_frontend.{n}.compression`: [optional]: Compression declarations
* `haproxy_frontend.{n}.compression.{n}.name`: [required]: The compression name (e.g. `algo`, `type`, `offload`)
* `haproxy_frontend.{n}.compression.{n}.value`: [required]: The compression value, (e.g. if name = algo : one of this values `identity`, `gzip`, `deflate`, `raw-deflate` / if name = type : list of mime type separated by space for example `text/html text/plain text/css` / if name = `offload` value is empty)
* `haproxy_frontend.{n}.errorfile`: [optional]: Errorfile declarations
* `haproxy_frontend.{n}.errorfile.{n}.code`: [required]: The HTTP status code. Currently, HAProxy is capable of generating codes 200, 400, 403, 408, 500, 502, 503, and 504 (e.g. `400`)
* `haproxy_frontend.{n}.errorfile.{n}.file`: [required]: A file containing the full HTTP response (e.g `/etc/haproxy/errors/400.http`)
* `haproxy_frontend.{n}.raw_options`: [default: `[]`]: Additional arbitrary lines to insert in the section

* `haproxy_backend`: [default: `[]`]: Back-end declarations
* `haproxy_backend.{n}.name`: [required]: The name of the section (e.g. `webservers`)
* `haproxy_backend.{n}.description`: [optional]: A description of the section (e.g. `Back-end with all (Apache) webservers`)
* `haproxy_backend.{n}.bind_process`:  [optional]: Limits the declaration to a certain set of processes numbers (e.g. `[all]`, `[1]`, `[2 ,3, 4]`)
* `haproxy_backend.{n}.mode`: [required]: Set the running mode or protocol of the section (e.g. `http`)
* `haproxy_backend.{n}.balance`: [required]: The load balancing algorithm to be used (e.g. `roundrobin`)
* `haproxy_backend.{n}.source`: [optional]: Set the source address or interface for connections from the proxy
* `haproxy_backend.{n}.option`: [optional]: Options to set (e.g. `[forwardfor]`)
* `haproxy_backend.{n}.no_option`: [optional]: Options to unset (e.g. `[redispatch]`)
* `haproxy_backend.{n}.http_check`: [optional]: Make HTTP health checks consider response contents or specific status codes (e.g. `expect status 403`)
* `haproxy_backend.{n}.stick`: [optional]: Stick declarations
* `haproxy_backend.{n}.stick.{n}.table`: [required]: Configure the stickiness table for the current section (e.g. `type ip size 500k`)
* `haproxy_backend.{n}.stick.{n}.stick_on`: [required]: Define a request pattern to associate a user to a server (e.g. `src`)
* `haproxy_backend.{n}.no_option`: [optional]: Options to unset (e.g. `[forceclose]`)
* `haproxy_backend.{n}.no_log`: [optional, default `false`]: Used when the logger list must be flushed. For example, if you don't want to inherit from the default logger list
* `haproxy_backend.{n}.tcp_check`: [optional]: Perform health checks using tcp-check send/expect sequences (e.g. `['expect string +OK\ POP3\ ready']`)
* `haproxy_backend.{n}.timeout`: [optional]: Timeout declarations
* `haproxy_backend.{n}.timeout.type`: [required]: The type (e.g. `server`)
* `haproxy_backend.{n}.timeout.timeout`: [required]: The timeout (in in milliseconds by default, but can be in any other unit if the number is suffixed by the unit) (e.g. `5000`, `50000`)
* `haproxy_backend.{n}.acl`: [optional]: Create an ACL check which can be later used in evaluations/conditionals
* `haproxy_backend.{n}.acl.{n}.string`: [required]: ACL entry to be used in conditional check later
* `haproxy_backend.{n}.reqadd`: [optional]: Adds headers at the end of the HTTP request
* `haproxy_backend.{n}.reqadd.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_backend.{n}.reqadd.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_backend.{n}.rspadd`: [optional]: Adds headers at the end of the HTTP response
* `haproxy_backend.{n}.rspadd.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_backend.{n}.rspadd.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_backend.{n}.reqdel`: [optional]: Delete all headers matching a regular expression in an HTTP request
* `haproxy_backend.{n}.reqdel.{n}.search`: [required]: The regular expression applied to HTTP headers and to the request line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_backend.{n}.reqdel.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_backend.{n}.reqidel`: [optional]: Delete all headers matching a regular expression in an HTTP request (ignore case)
* `haproxy_backend.{n}.reqidel.{n}.search`: [required]: The regular expression applied to HTTP headers and to the request line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_backend.{n}.reqidel.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_backend.{n}.rspdel`: [optional]: Delete all headers matching a regular expression in an HTTP response
* `haproxy_backend.{n}.rspdel.{n}.search`: [required]: The regular expression applied to HTTP headers and to the response line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_backend.{n}.rspdel.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_backend.{n}.rspidel`: [optional]: Delete all headers matching a regular expression in an HTTP response (ignore case)
* `haproxy_backend.{n}.rspidel.{n}.search`: [required]: The regular expression applied to HTTP headers and to the response line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_backend.{n}.rspidel.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_backend.{n}.reqrep`: [optional]: Replace a regular expression with a string in an HTTP request line
* `haproxy_backend.{n}.reqrep.{n}.search`: [required]: The regular expression applied to HTTP headers and to the request line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_backend.{n}.reqrep.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_backend.{n}.reqrep.{n}.cond`: [optional]: Matching condition built from ACLs
* `haproxy_backend.{n}.reqirep`: [optional]: Replace a regular expression with a string in an HTTP request line (ignore case)
* `haproxy_backend.{n}.reqirep.{n}.search`: [required]: The regular expression applied to HTTP headers and to the request line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_backend.{n}.reqirep.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_backend.{n}.reqirep.{n}.cond`: [optional]: Matching condition built from ACLs
* `haproxy_backend.{n}.rsprep`: [optional]: Replace a regular expression with a string in an HTTP response line
* `haproxy_backend.{n}.rsprep.{n}.search`: [required]: The regular expression applied to HTTP headers and to the response line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_backend.{n}.rsprep.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_backend.{n}.rsprep.{n}.cond`: [optional]: Matching condition built from ACLs
* `haproxy_backend.{n}.rspirep`: [optional]: Replace a regular expression with a string in an HTTP response line (ignore case)
* `haproxy_backend.{n}.rspirep.{n}.search`: [required]: The regular expression applied to HTTP headers and to the response line. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_backend.{n}.rspirep.{n}.string`: [required]: The complete line to be added. Any space or known delimiter must be escaped using a backslash (`'\'`) (in version < 1.6)
* `haproxy_backend.{n}.rspirep.{n}.cond`: [optional]: Matching condition built from ACLs
* `haproxy_backend.{n}.cookie`: [optional]: Enable cookie-based persistence in a backend (e.g. `JSESSIONID prefix nocache`)
* `haproxy_backend.{n}.http_request`: [optional]: Access control for Layer 7 requests
* `haproxy_backend.{n}.http_request.{n}.action`: [required]: The rules action (e.g. `add-header`)
* `haproxy_backend.{n}.http_request.{n}.param`: [optional]: The complete line to be added (e.g. `X-Forwarded-Proto https`)
* `haproxy_backend.{n}.http_request.{n}.cond`: [optional]: A matching condition built from ACLs (e.g. `if { ssl_fc }`)
* `haproxy_backend.{n}.http_response`: [optional]: Access control for Layer 7 responses
* `haproxy_backend.{n}.http_response.{n}.action`: [required]: The rules action (e.g. `del-header`)
* `haproxy_backend.{n}.http_response.{n}.param`: [optional]: The complete line to be added (e.g. `X-Varnish`)
* `haproxy_backend.{n}.http_response.{n}.cond`: [optional]: A matching condition built from ACLs
* `haproxy_backend.{n}.tcp_request_content`: [optional]: Perform an action on a new session depending on a layer 4-7 condition.
* `haproxy_backend.{n}.tcp_request_content.{n}.action`: [required]: The action for the `tcp-request content` rule.
* `haproxy_backend.{n}.tcp_request_content.{n}.cond`: [optional]: A matching condition for the `tcp-request content` rule.
* `haproxy_backend.{n}.tcp_request_inspect_delay`: [optional]: Set the maximum allowed time to wait for data during content inspection.
* `haproxy_backend.{n}.tcp_request_inspect_delay.{n}.timeout`: [required]: The timeout value in millisecond for the `tcp-request inspect-delay` rule.
* `haproxy_backend.{n}.stats`: [optional]: Stats declarations
* `haproxy_backend.{n}.stats.enable`: [required]: Enables statistics reporting with default settings
* `haproxy_backend.{n}.stats.uri`: [optional, default `/`]: Define the URI prefix to access statistics
* `haproxy_backend.{n}.stats.options`: [optional]: List of boolean stats options (e.g. `hide-version`, `show-node`, `show-desc`, `show-legends`)
* `haproxy_backend.{n}.stats.refresh`: [optional]: Defined the refresh delay, specified in seconds (e.g. `5s`)
* `haproxy_backend.{n}.stats.admin`: [optional]: Define / enable admin part of web interface with conditional attached
* `haproxy_backend.{n}.stats.auth`: [optional]: Auth declarations
* `haproxy_backend.{n}.stats.auth.{n}.user`: [required]: A user name to grant access to
* `haproxy_backend.{n}.stats.auth.{n}.passwd`: [required]: The cleartext password associated to this user
* `haproxy_backend.{n}.compression`: [optional]: Compression declarations
* `haproxy_backend.{n}.compression.{n}.name`: [required]: The compression name (e.g. `algo`, `type`, `offload`)
* `haproxy_backend.{n}.compression.{n}.value`: [required]: The compression value, (e.g. if name = algo : one of this values `identity`, `gzip`, `deflate`, `raw-deflate` / if name = type : list of mime type separated by space for example `text/html text/plain text/css` / if name = `offload` value is empty)
* `haproxy_backend.{n}.server`: [optional]: Server declarations
* `haproxy_backend.{n}.server.{n}.name`: [required]: The internal name assigned to this server
* `haproxy_backend.{n}.server.{n}.listen`: [required]: Defines a listening address and/or ports
* `haproxy_backend.{n}.server.{n}.param`: [optional]: A list of parameters for this server
* `haproxy_backend.{n}.errorfile`: [optional]: Errorfile declarations
* `haproxy_backend.{n}.errorfile.{n}.code`: [required]: The HTTP status code. Currently, HAProxy is capable of generating codes 200, 400, 403, 408, 500, 502, 503, and 504 (e.g. `400`)
* `haproxy_backend.{n}.errorfile.{n}.file`: [required]: A file containing the full HTTP response (e.g `/etc/haproxy/errors/400.http`)
* `haproxy_backend.{n}.default_server_params`: [optional]: Default server params applied for each server for this particular backend entry.
* `haproxy_backend.{n}.raw_options`: [default: `[]`]: Additional arbitrary lines to insert in the section

* `haproxy_userlists`: [default: `[]`]: Userlist declarations
* `haproxy_userlists.{n}.name`: [required]: The name of the userlist
* `haproxy_userlists.{n}.users`: [required] Userlist users declarations
* `haproxy_userlists.{n}.users.{n}.name`: [required] The username of this user
* `haproxy_userlists.{n}.users.{n}.password`: [optional] Password hash of this user. **One of `password` or `insecure_password` must be set**
* `haproxy_userlists.{n}.users.{n}.insecure_password`: [optional] Plaintext password of this user. **One of `password` or `insecure_password` must be set**
* `haproxy_userlists.{n}.users.{n}.groups`: [optional] List of groups to add the user to

* `haproxy_acl_files`: [default: `[]`]: ACL file declarations
* `haproxy_acl_files.{n}.dest`: [required]: The remote path of the file (e.g. `/etc/haproxy/acl/api.map`)
* `haproxy_acl_files.{n}.content`: [default: `[]`]: The content (lines) of the file (e.g. `['v1.0 be_alpha', 'v1.1 be_bravo']`)

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
      #
      # This will execute http checks against different port than server is pointing to.
      - name: brokers
        mode: tcp
        balance: first
        option:
          - 'httpchk GET /'
        default_server_params:
          - port 8161
          - inter 2s
          - downinter 5s
          - rise 3
          - fall 2
        server:
          - name: mqtt-1
            listen: "{{ ansible_lo['ipv4']['address'] }}:1883"
            param:
              - check

          - name: mqtt-2
            listen: "{{ ansible_lo['ipv4']['address'] }}:1883"
            param:
              - check
              - backup
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

## Overriding configuration template

If you can't customize via variables because an option isn't exposed, you can override the template used to generate the haproxy configuration file.

```yaml
haproxy_conf_template: "etc/haproxy/haproxy.cfg.j2"
```

You can either copy and modify the provided template, or extend it with [Jinja2 template inheritance](http://jinja.pocoo.org/docs/2.9/templates/#template-inheritance) and override the specific template block you need to change.

#### License

MIT

#### Author Information

Mischa ter Smitten (based on work of [FloeDesignTechnologies](https://github.com/FloeDesignTechnologies))

#### Feedback, bug-reports, requests, ...

Are [welcome](https://github.com/Oefenweb/ansible-haproxy/issues)!

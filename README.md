## haproxy

[![Build Status](https://travis-ci.org/Oefenweb/ansible-haproxy.svg?branch=master)](https://travis-ci.org/Oefenweb/ansible-haproxy) [![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-haproxy-blue.svg)](https://galaxy.ansible.com/list#/roles/3856)

Set up the latest version of [HAProxy](http://www.haproxy.org/) in Ubuntu systems.

#### Requirements

* `python-apt`

#### Variables

* `haproxy_install`: [default: `[]`]: Additional packages to install

## Dependencies

None

#### Example

```yaml
---
- hosts: all
  roles:
  - haproxy
```

#### License

MIT

#### Author Information

Mischa ter Smitten (based on work of [FloeDesignTechnologies](https://github.com/FloeDesignTechnologies))

#### Feedback, bug-reports, requests, ...

Are [welcome](https://github.com/Oefenweb/ansible-haproxy/issues)!

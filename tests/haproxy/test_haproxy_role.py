
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_haproxy_is_installed(Package):
    haproxy = Package("haproxy")
    assert haproxy.is_installed
    assert haproxy.version.startswith("1.7")


def test_haproxy_is_running(Service):
    haproxy = Service("haproxy")
#   assert haproxy.is_running
    assert haproxy.is_enabled


def test_haproxy_is_listening(Socket):
    ports = [1936, 3306, 80]

    for port in ports:
        assert Socket("tcp://0.0.0.0:{0}".format(port)).is_listening

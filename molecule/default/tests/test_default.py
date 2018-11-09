import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ddclient_package(host):
    ddclient_package = host.package('ddclient')
    assert ddclient_package.is_installed


def test_ddclient_service(host):
    ddclient_service = host.service('ddclient')
    assert ddclient_service.is_enabled


def test_ddclient_config(host):
    ddclient_config = host.file('/etc/ddclient.conf')

    assert ddclient_config.exists
    assert ddclient_config.user == 'root'
    assert ddclient_config.group == 'root'
    assert ddclient_config.contains('^protocol=*')

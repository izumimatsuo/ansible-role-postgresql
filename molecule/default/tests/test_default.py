import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_postgresql_is_installed(host):
    package = host.package("postgresql11")
    assert package.is_installed
    assert package.version.startswith("11")


def test_postgresql_running_and_enabled(host):
    service = host.service("postgresql-11")
    assert service.is_running
    assert not service.is_enabled


def test_postgresql_is_listen(host):
    assert host.socket("tcp://0.0.0.0:5432").is_listening

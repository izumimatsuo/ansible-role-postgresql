# -*- coding:utf8 -*-

def test_postgresql_is_installed(host):
    postgresql = host.package("postgresql96")
    assert postgresql.is_installed
    assert postgresql.version.startswith("9.6")

def test_postgresql_running_and_enabled(host):
    postgresql = host.service("postgresql-9.6")
    assert postgresql.is_running
    assert postgresql.is_enabled

def test_postgresql_is_listen(host):
    assert host.socket("tcp://127.0.0.1:5432").is_listening

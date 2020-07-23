# ansible-role-postgresql [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-postgresql.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-postgresql)

CentOS 7 に postgresql を導入する ansible role です。

pg_enable_replication を設定することでレプリケーションに必要な設定をおこなう

- レプリケーションユーザの登録
- pg_hab.conf および postgresql.conf の設定追加
- 運用に必要なツールの導入

レプリケーション適用すると運用に必要な以下のツールが導入される

- pg_start_replication.sh プライマリサーバの起動
- pg_join_replication.sh セカンダリサーバの追加

## 設定項目

以下の設定項目は上書き可能。

| 項目名                | デフォルト値 | 説明       |
| --------------------- | ------------ | ---------- |
| pg_listen_port        | 5432         | ポート番号 |
| pg_enable_replication | no           | レプリケーション適用有無 |
| pg_primary_host       | none         | プライマリーホスト |
| pg_primary_port       | 5432         | プライマリーホストのポート番号 |
| pg_replication_user   | repl_user    | レプリケーションユーザ |
| pg_replication_passwd | password     | レプリケーションユーザのパスワード |
| pg_replication_allow_ipaddr | none   | レプリケーション許可IPアドレス |

# ansible-role-postgresql [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-postgresql.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-postgresql)

CentOS 7 に postgresql を導入する ansible role です。

pgsql_cluster_hostnames および pgsql_replication_* を設定することでレプリケーション機能を設定できる

- レプリケーションユーザの登録
- pg_hab.conf の設定
- レプリケーションは非同期に設定

pacemaker_cluster_info を設定することで上記に加えて 1+1 (Master/Standby) クラスタを構築できる

- クラスタリングミドルは pacemaker/corosync を適用
- レプリケーションは同期に設定

1+1 (Master/Standby) クラスタでの障害時の動作は以下のとおり

1. Standby が障害の場合は VIP は移動せず、Master は非同期レプリケーションへ移行
1. Standby を復旧すると Master は再度、同期レプリケーションへ移行
1. Master で障害の場合は Standby へ VIP が移動して非同期レプリケーションへ移行
1. 旧Master を復旧すると、新Standby として組み込まれ同期レプケーションへ移行

## 設定項目

以下の設定項目は上書き可能。

| 項目名                   | デフォルト値 | 説明       |
| ------------------------ | ------------ | ---------- |
| pgsql_listen_port        | 5432         | ポート番号 |
| pgsql_user               | developer    | データベースユーザ |
| pgsql_passwd             | password     | データベースユーザのパスワード |
| pgsql_database           | development  | データベース名 |
| pgsql_cluster_hostnames  | None         | クラスタを構成するサーバ（inventory_name）のリスト |
| pgsql_replication_user   | repl_user    | レプリケーションユーザ |
| pgsql_replication_passwd | password     | レプリケーションユーザのパスワード |
| pgsql_replication_allow_ipaddr | None   | レプリケーション許可IPアドレス |
| pacemaker_cluster_info   | None         | VIP情報 |
| pacemaker_cluster_name   | pgsqlcluster | クラスタ名 |
| pacemaker_hacluster_password | password | クラスタ管理ユーザのパスワード |

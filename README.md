# ansible-role-postgresql [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-postgresql.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-postgresql)

CentOS 7 に postgresql を導入する ansible role です。

pg_enable_replication を設定することで (同期) レプリケーションに必要な設定をおこなう

- レプリケーションユーザの登録
- pg_hab.conf および postgresql.conf の設定追加
- 運用に必要なツールの導入
- クラスタリングミドル (keepalived) の導入

起動時の動作は以下となる

1. 1台目の keepalived 起動 (MASTER_STATE へ遷移)
1. pg_primary_host の内容を VIP として設定
1. pg_start_replication.sh を実行 (postgresql が primary で起動)
1. 非同期レプリケーション開始
1. 2台目の keepalived 起動 (BACKUP_STATE へ遷移)
1. pg_join_replication.sh を実行 (postgresql が secondary で起動)
1. primary はレプリケーション動作を非同期から同期へ移行

障害時の動作は以下のとおり

1. secandary が障害の場合は VIP は移動せず、primary は非同期レプリケーションに移行
1. secandary が復旧すると primary は再度、同期レプリケーションへ移行
1. primary で障害の場合は secandary へ VIP が移動して非同期レプリケーションへ移行
1. 旧primary が復旧すると、新secandary として組み込まれ同期レプケーションへ移行

## 設定項目

以下の設定項目は上書き可能。

| 項目名                | デフォルト値 | 説明       |
| --------------------- | ------------ | ---------- |
| pg_listen_port        | 5432         | ポート番号 |
| pg_enable_replication | no           | レプリケーション適用有無 |
| pg_primary_host       | none         | プライマリーホスト (VIP) |
| pg_primary_port       | 5432         | プライマリーホストのポート番号 |
| pg_replication_user   | repl_user    | レプリケーションユーザ |
| pg_replication_passwd | password     | レプリケーションユーザのパスワード |
| pg_replication_allow_ipaddr | none   | レプリケーション許可IPアドレス |
| pg_check_interface    | none         | ヘルスチェック用NIC |

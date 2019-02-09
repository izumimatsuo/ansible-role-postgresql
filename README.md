# ansible-role-postgresql

CentOS 7 に postgresql を構築する ansible role です。

## 設定項目

以下の設定項目は上書き可能。

項目名           |デフォルト値|説明
-----------------|------------|----------
pg_listen_port   |5432        |ポート番号
pg_version       |9.6         |バージョン
pg_package_rpm   |※1         |パッケージ URL
pg_package_base  |postgresql96|パッケージベース名

※1 https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm

## ビルド

以下のいづれかで ansible-playbook と testinfra を実行可能。

1) docker-compose でビルド実行

``` $ ./build.sh ```

2) gitlab-runner でビルド実行

``` $ gitlab-runner exec docker --docker-volumes /var/run/docker.sock:/var/run/docker.sock ansible_build ```

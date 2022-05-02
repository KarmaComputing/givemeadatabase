#day0

```

./day0.sh segfault.app 3 1 cx31 ubuntu-20.04
```

From local machine (details: https://docs.pingcap.com/tidb/stable/production-deployment-using-tiup#method-1-deploy-tiup-online)

```
curl --proto '=https' --tlsv1.2 -sSf https://tiup-mirrors.pingcap.com/install.sh | sh

tiup cluster

tiup update --self && tiup update cluster

tiup --binary cluster
```

```
for HOST in $(cat servers.txt)
do
  ssh root@$HOST -C "apt-get update && apt install -y numactl pwgen"
done

```

```
tiup cluster check ./topology.yaml --user root
```

deploy
```
tiup cluster deploy tidb-test v5.4.0 ./topology.yaml --user root
```

start it
```
tiup cluster start tidb-test --init
# get initial password
```

# Visit dashboard

http://$TIDB_PANEL_ADDRESS:2379/dashboard/#/signin

# Verify can connect to the database remotely

```
$ mysql -u root -h $TIDB_HOSTNAME -P 4000 -p
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 5
Server version: 5.7.25-TiDB-v5.4.0 TiDB Server (Apache License 2.0) Community Edition, MySQL 5.7 compatible

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [(none)]> create database yolo;
Query OK, 0 rows affected (0.573 sec)
```

# remove

```
./destroy-all.sh
```
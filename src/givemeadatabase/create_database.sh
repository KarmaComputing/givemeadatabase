#!/bin/bash

USERNAME=user_$(pwgen --ambiguous 5 1)
PASSOWRD=$(pwgen --ambiguous 15 1)
DATABASE_NAME=db_$(pwgen --ambiguous 3 1)_ts_$EPOCHSECONDS

#mysql --connect-timeout 5 -u root -h $TIDB_HOSTNAME -P $TIDB_PORT -p$TIDB_ROOT_PASSWORD -e "CREATE DATABASE testing;"
mysql --connect-timeout 5 -u root -h $TIDB_HOSTNAME -P $TIDB_PORT -p$TIDB_ROOT_PASSWORD -e "CREATE DATABASE $DATABASE_NAME;"

mysql --connect-timeout 5 -u root -h $TIDB_HOSTNAME -P $TIDB_PORT -p$TIDB_ROOT_PASSWORD -e "CREATE USER IF NOT EXISTS '$USERNAME'@'%' IDENTIFIED BY '$PASSOWRD';"


mysql --connect-timeout 5 -u root -h $TIDB_HOSTNAME -P $TIDB_PORT -p$TIDB_ROOT_PASSWORD -e "GRANT ALL PRIVILEGES ON $DATABASE_NAME.* TO '$USERNAME'@'%';
;"

# Return connection details as json string
printf '{"username":"%s","password":"%s","hostname":"%s","port":"%s", "db_name":"%s"}\n' "$USERNAME" "$PASSOWRD" "$TIDB_HOSTNAME" "$TIDB_PORT" "$DATABASE_NAME"

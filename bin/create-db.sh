#!/bin/sh

# Create Application Database and User
# ---
# This script will use the `psql` command to run SQL commands that
# will create the needed database and user for this application.
# A running PostgreSQL server is necessary.
#
# NOTE: You only need to run this script once.
#
# Run with the following command in the project's root directory:
# $ sh bin/create-db.sh

DEV=true

if [ "$1" == "test" ]; then
  DEV=false
fi


# create user for the application
psql postgres -c 'CREATE USER LCNapp_user;'

# create development database and grant access to application user
if [ $DEV == true ]; then
  psql postgres -c 'CREATE DATABASE LCNapp;'
  psql postgres -c 'GRANT ALL PRIVILEGES ON DATABASE "LCNapp" to LCNapp_user;'
fi

# create test database and grant access to application user
psql postgres -c 'CREATE DATABASE LCNapp_test;'
psql postgres -c 'GRANT ALL PRIVILEGES ON DATABASE "LCNapp_test" to LCNapp_user;'

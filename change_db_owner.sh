#!/bin/bash

usage()
{
cat << EOF
usage: $0 options
This script set ownership for all table, sequence and views for a given database
Credit: Based on http://stackoverflow.com/a/2686185/305019 by Alex Soto
        Also merged changes from @sharoonthomas
OPTIONS:
   -h      Show this message
   -d      Database name
   -o      Owner
EOF
}

DB_NAME=
NEW_OWNER=

while getopts "hd:o:" OPTION 
do
    case $OPTION in
        h)  
            usage
            exit 1
            ;;  
        d)  
            DB_NAME=$OPTARG
            ;;  
        o)  
            NEW_OWNER=$OPTARG
            ;;  
    esac
done

if [[ -z $DB_NAME ]] || [[ -z $NEW_OWNER ]]
then
     usage
     exit 1
fi

for tbl in `psql -qAt -U postgres -c "select schemaname || '.' || tablename from pg_tables where schemaname <> 'pg_catalog' and schemaname <> 'information_schema';" ${DB_NAME}` \
           `psql -qAt -U postgres -c "select sequence_schema || '.' || sequence_name from information_schema.sequences where sequence_schema <> 'pg_catalog' and sequence_schema <> 'information_schema';" ${DB_NAME}` \
           `psql -qAt -U postgres -c "select table_schema || '.' || table_name from information_schema.views where table_schema <> 'pg_catalog' and table_schema <> 'information_schema';" ${DB_NAME}` ;
do  
    psql -U postgres -c "alter table $tbl owner to ${NEW_OWNER}" ${DB_NAME} ;
done

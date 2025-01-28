#!/bin/bash

#backup script

BACKUP_SRC = "/tmp"
BACKUP_DST = "/backups"
BACKUP_DATE = $(date +%Y%m%d%H%M%S)

mkdir -p "$BACKUP_DST/$BACKUP_DATE_"
#using tar command for backing up files 
tar -czf "$BACKUP_DST/$BACKUP_DATE_/$BACKUP_FILENAME" "$BACKUP_SRC"

if [$ -eq 0] then 
        echo "Backup successful: $BACKUP_FILENAME" #succesful backup
else 
        echo "Backup failed"


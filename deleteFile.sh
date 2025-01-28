#!/bin/bash

deleteFile() {
    echo 'Delete Files'
    echo 'Enter name of file to be deleted: '
    read filename

    rm $filename
    echo "File: $filename has been deleted"

}
deleteFile


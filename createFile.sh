#!/bin/bash
createFile() {
    echo 'Create a New File'
    echo 'Enter name of new file (in .txt format): '
    read filename

    touch $filename

    echo "File: $filename has been created for you."
}

#executing script
createFile

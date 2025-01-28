#!/bin/bash

createFileInPath(){
    echo 'Create file with path'
    echo 'Enter path for new file (/path_to_directory/filename.txt): '
    read path

    touch $path
    echo "File has been created. It is located in $path"
}
#executing script
createFileInPath


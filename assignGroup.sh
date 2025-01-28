#!/bin/bash

assignGroup() {
    echo 'This function is to assign a group ownership of a file/directory.'
    echo 'Enter name of the group: '
    read groupname

    echo 'Enter name of file/directory: '
    read filename

    sudo chgrp $groupname $filename
    echo "Complete! Group: $groupname now has ownership of file/directory: $filename"

}

#executing script
assignGroup
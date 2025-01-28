#!/bin/bash

addGroup() {
    echo 'Enter group name: '
    read groupname
    
    echo 'Enter Group ID: '
    read groupid

    sudo groupadd -g $groupid $groupname

    echo "COMPLETE! Group $groupname with ID $groupid has been added to the system."

}
#executing script
addGroup

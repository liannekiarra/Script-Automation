#!/bin/bash

removeUserFromGroup() {
    echo 'Enter username to be removed: '
    read username
    echo ' Enter group name to remove user from: '
    read groupname

    sudo gpasswd --delete $username $groupname
    echo "Complete! User: $username has been deleted from Group: $groupname."

}
#executing script

removeUserFromGroup
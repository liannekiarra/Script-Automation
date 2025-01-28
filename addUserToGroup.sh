#!/bin/bash

addUsertoGroup() {
    echo 'Add a user into a group.'
    echo 'Enter username to be added: '
    read username
    echo 'Enter group name to add the user: '
    read groupname

    sudo usermod --append --groups $groupname $username
    echo "Complete! User $username has been added to group $groupname."


}
#executing script
addUsertoGroup
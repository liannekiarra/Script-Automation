#!/bin/bash

deleteGroup() {
    echo 'Enter name fo group to delete: '
    read groupname

    sudo groupdel $groupname
    echo "Group $groupname has been deleted from the system."

}

#executing script

deleteGroup
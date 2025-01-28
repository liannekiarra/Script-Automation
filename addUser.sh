#!/bin/bash

# Function to create a new user
addUser() {
    

    echo 'Enter new username: '
    read username
    echo 'Enter password for this user: '
    read password


    # Create the user with the specified username
    sudo useradd -m -s /bin/bash $username

    # Set the user's password
    echo "$username:$password" | sudo chpasswd

    echo "User '$username' has been created with the password '$password'"
}

#executing script
addUser
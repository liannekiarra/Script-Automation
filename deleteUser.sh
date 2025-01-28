#!/bin/bash

#!/bin/bash

echo "Enter Username to delete: "
read username
echo "Enter your password: "
read adminPassword

deleteUser() {
    echo $adminPassword | sudo -S deluser $username
}

#executing script
deleteUser
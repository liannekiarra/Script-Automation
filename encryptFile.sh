#!/bin/bash
encryptFile() {
    echo 'Enter filename to be encrypted: '
    read filename

    gpg -c $filename
    echo "file has been successfully encrypted! Your encrypted file is: $filename.gpg"

}
encryptFile


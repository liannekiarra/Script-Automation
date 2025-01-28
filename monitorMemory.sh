#!/bin/bash

monitorMemory() {

    echo 'DISPLAYING MEMORY INFRORMATION'
    echo 'Enter PDF filename: '
    read $filename

    vmstat -a > $filename.pdf #returning a pdf file


}
monitorMemory

#!/bin/bash

monitorDisk() {

    echo 'Enter PDF filename: '
    read filename
    echo 'Displaying statistics of Disk'
    vmstat -d > $filename.pdf #returning a pdf file

}
monitorDisk
#!/bin/bash

#Reveal Free Memory Space

monitorFreeMemory(){
    echo 'Enter name of pdf: '
    read filename

    free > $filename.pdf #returning a pdf file

}
monitorFreeMemory
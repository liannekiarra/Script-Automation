#!/bin/bash

# 1) IOSTAT -x : gives I/O device report utilisation

ioReport() {
    echo 'Giving I/O device report utilisation'
    iostat -x
}

# 2) IOSTAT -c : This gives information about CPU statistic

cpuStats() {
    echo 'Giving CPU statistics'
    iostat -c
}

ioReport
cpuStats



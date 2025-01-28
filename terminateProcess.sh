#!/bin/bash

terminateProcess() {

    echo 'Enter the Process ID: '
    read pid
    kill $pid
    echo "Process $pid has been terminated."
}

terminateProcess

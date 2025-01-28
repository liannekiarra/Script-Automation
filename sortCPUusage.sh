#!/bin/bash 

sort() {
    ps -eo pid,%cpu --sort=-%cpu | head -10

}
sort

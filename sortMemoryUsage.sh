#!/bin/bash

sort() {
    ps -eo pid,%mem --sort=-%mem | head -10

}
sort


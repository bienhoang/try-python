#!/usr/bin/env python3

count = 0


def add_count(c):
    global count
    count = c
    print(count)

add_count(5)
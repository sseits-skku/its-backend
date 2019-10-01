#!/bin/bash
strings /dev/urandom | grep -o '[[:print:]]' | grep -v \  | grep -v \' | grep -v \"  | grep -F -v \\ | head -n 64 | tr -d '\n' && echo
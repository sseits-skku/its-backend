#!/bin/bash

cd server/settings/
gpg -d development.py.asc
gpg -d production.py.asc
cd ../..

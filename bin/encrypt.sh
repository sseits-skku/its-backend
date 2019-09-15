#!/bin/bash

cd server/settings/
gpg -sear 73DC25230A8FBCB09F840CBBF2C50C577D6A82A9 development.py
gpg -sear 73DC25230A8FBCB09F840CBBF2C50C577D6A82A9 production.py
cd ../..

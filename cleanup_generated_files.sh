#!/usr/bin/env bash

shopt -s extglob

rm -r docs/
rm -r priceloop_api/!(utils)
rm -r test/
rm -r test/!(test_utils.py)
rm test-requirements.txt
rm tox.ini

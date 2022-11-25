#!/usr/bin/env bash

shopt -s extglob

rm -r docs/
rm -r priceloop_api/!(utils)
rm -r test/
rm test-requirements.txt
rm tox.ini

#/usr/bin/env bash

set -Eeuo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"

if [[ "$(git diff --stat)" != "" ]]; then
  echo 'git repository is dirty, exiting.'
  exit 1
fi

version=$(cat ./openapi.json | jq -r '.info.version')
version_numbers=$(echo $version | sed s/^v//)

# replace version in setup.py
sed "s/version=.*$/version=$version_numbers/" -i setup.py

# regenerate the whole python project
rm -rf priceloop-api-python
openapi-python-client generate --path openapi.json --config config.yml

# copy over python code from generated project
rm -rf priceloop_api
cp -r priceloop-api-python/priceloop_api priceloop_api

# rescue custom files
git checkout priceloop_api/priceloop

#!/usr/bin/env bash
set -eo pipefail

if [ ! "$1" ]; then
  echo "Usage $0 VERSION"
  exit 1
fi

VERSION=$1

if ! echo "${VERSION}" | grep -E -q '^[0-9.]+$'; then
  echo 'Invalid version'
  exit 1
fi

if ! git diff --quiet; then
  echo "Not clean"
  exit 1
fi


echo "__version__ = '${VERSION}'" > src/pi5ir/version.py

pytest || exit 1

git commit src/pi5ir/version.py -m "v${VERSION}"
git tag "v${VERSION}"

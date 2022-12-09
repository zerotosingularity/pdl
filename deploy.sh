#!/bin/bash

./test.sh

if [ $? -eq 0 ]
then
  python3 setup.py sdist bdist_wheel
  twine upload dist/*  --skip-existing
else
  echo "Unbale to deploy because tests are failing"
  exit -1
fi





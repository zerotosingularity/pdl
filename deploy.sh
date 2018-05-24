#!/bin/bash

./test.sh

if [ $? -eq 0 ]
then
  python setup.py sdist upload
else
  echo "Unbale to deploy because tests are failing"
  exit -1
fi





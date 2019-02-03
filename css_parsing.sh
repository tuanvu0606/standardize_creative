#!/bin/sh

DIRECTORY="/home/ec2-user/standardize_creative/css"

if [ -d "$DIRECTORY" ]; then
  # Control will enter here if $DIRECTORY exists.
  echo "CSS folder exist"
  if [ -f "$DIRECTORY/*.css" ]; then
    touch 
  else
    echo "CSS File not found!"  
  fi
else
  mkdir $DIRECTORY
fi

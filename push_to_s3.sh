#!/bin/sh

campaign=$(jq '.campaign[0].name' config.json) 
width=$(jq '.width' config.json) 
height=$(jq '.height' config.json) 
DSP=$(jq '.DSP' config.json)
build=$(jq '.build' config.json) 

campaign=$(echo $campaign | tr -d '"')
width=$(echo $width | tr -d '"')
height=$(echo $height | tr -d '"')
DSP=$(echo $DSP | tr -d '"')
build=$(echo $build | tr -d '"')

echo $campaign
echo $width
echo $height
echo $DSP
echo $build

echo /var/lib/jenkins/jobs/${JOB_NAME}/builds/${build}/archive

ls -la /var/lib/jenkins/jobs/${JOB_NAME}/builds/${build}/archive

echo s3://tuan.vu.yoose/Campaigns/$campaign-${width}x$height/$DSP/${build}

# ~/.local/bin/aws s3 cp /var/lib/jenkins/jobs/${JOB_NAME}/builds/${BUILD_NUMBER}/archive s3://tuan.vu.yoose/Campaigns/${params.CAMPAIGN}/${BUILD_NUMBER} --recursive --exclude "*" --include "*.html" --include "*.js" --include "*.css" --acl public-read


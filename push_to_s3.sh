#!/bin/sh

campaign=$(jq '.campaign[0].name' config.json)
width=$(jq '.width' config.json)
height=$(jq '.height' config.json)
DSP=$(jq '.DSP' config.json)
echo $campaign
echo $width
echo $height
echo $DSP



~/.local/bin/aws s3 cp /var/lib/jenkins/jobs/${JOB_NAME}/builds/${BUILD_NUMBER}/archive s3://tuan.vu.yoose/Campaigns/${params.CAMPAIGN}/${BUILD_NUMBER} --recursive --exclude "*" --include "*.html" --include "*.js" --include "*.css" --acl public-read


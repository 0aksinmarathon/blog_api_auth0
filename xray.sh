#!/bin/bash
curl https://s3.dualstack.ap-northeast-1.amazonaws.com/aws-xray-assets.ap-northeast-1/xray-daemon/aws-xray-daemon-3.x.rpm -o /home/ec2-user/xray.rpm
yum install -y /home/ec2-user/xray.rpm

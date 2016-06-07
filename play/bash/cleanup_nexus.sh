#!/bin/bash
#
NUM_OF_DAYS=${1:?"I need a number of days, e.g., 90"}
echo $NUM_OF_DAYS


TOPDIRS="\
/home/ubuntu/sonatype-work/nexus/storage/releases/com/cloudcar/justdrive/client/ios_justDrive_app \
/home/ubuntu/sonatype-work/nexus/storage/releases/com/cloudcar/justdrive/client/ios_justDrive_jlr \
/home/ubuntu/sonatype-work/nexus/storage/releases/com/cloudcar/justdrive/client/ios_JustDriveSDKDemo_demo \
/home/ubuntu/sonatype-work/nexus/storage/releases/com/cloudcar/justdrive/client/JDWebApp \
/home/ubuntu/sonatype-work/nexus/storage/releases/com/cloudcar/justdrive/client/JustDriveApk \
/home/ubuntu/sonatype-work/nexus/storage/releases/com/cloudcar/justdrive/cloudservices \
/home/ubuntu/sonatype-work/nexus/storage/releases/com/cloudcar/justdrive/servermain/NodeJS \
"

#0 0 * * 1-5 find /path/to/files -name filename* -mtime +183 -exec rm {} \; > /home/someuser/cronlogs/clean_tmp_dir.log

#0 0 * * 1-5 find  $TOPDIR -type d -mtime +183 -exec rm {} \; > /home/someuser/cronlogs/clean_tmp_dir.log

#0 0 * * 1-5 find  $TOPDIR -type d -mtime +90  > ~/cronlogs/cleanup_nexus.`date +%Y%m%d_%H%M%S`.log

#### woeking one:
#### 35 18 * * 3  /home/ubuntu/bin/cleannup_nexus.sh 90 > /home/ubuntu/cronlogs/cron.log.`date +\%Y\%m\%d_\%H\%M\%S` 2>&1

for dir in $TOPDIRS; do
  echo -----------------
  echo Processing $dir
  echo -----------------
  find $dir -type d -mtime +$NUM_OF_DAYS -ls
  find $dir -type d -mtime +$NUM_OF_DAYS -exec /bin/rm -rf {} \;
#  find $dir -type d -mtime +$NUM_OF_DAYS  -ls
#  find $dir -type d -mtime +$NUM_OF_DAYS
done


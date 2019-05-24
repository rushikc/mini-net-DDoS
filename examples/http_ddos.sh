#!/bin/sh 
# wget output file 
FILE=dailyinfo.20180317 

# wget log file 
LOGFILE=wget.log 
while true 
do 
        echo "Press CTRL+C to stop the script execution" 
        # wget download url 
        URL=http://10.0.0.7:8000 
        #cd $DIR 
        wget $URL -O $FILE -o $LOGFILE
        # sleep 2
done 


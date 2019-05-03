#!/bin/bash
path="/home/pi/Pictures/img_from_bot/*"
past=`ls $path`
if [ "1" = $(pgrep -c $(basename $0 .sh)) ]; then
    while :
        do
        now=`ls $path`
        if [[ $now != $past ]]; then
            sudo pkill -9 -x fbi
	    sudo fbi -T 1 -a -noverbose -t 30 -u -blend 4000 ${path}
	fi
	past=$now
        sleep 5;
    done
fi

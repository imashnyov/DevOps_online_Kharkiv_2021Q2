#!/bin/bash
log_out=out_script2
awk '{print $4, $1}' $1 | sort | uniq -c | sort -gr > $log_out
{
read line1    
} < $log_out
echo $line1
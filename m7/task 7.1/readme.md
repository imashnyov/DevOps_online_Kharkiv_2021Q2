 ### Linux administration with bash

 #### Created a scripts to answer the following question, using Apache example log.

 1. From which ip were the most requests:
   
ʼʼʼ 
#!/bin/bash
log_out=out_script1
grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" $1 | sort | uniq -c | sort -gr > $log_out
{
read line1    
} < $log_out
echo $line1 > 
ʼʼʼ

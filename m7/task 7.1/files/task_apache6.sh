#!/bin/bash
awk -vFPAT='([^ ]+)|("[^"]+")' '{print $1, $10}' $1 | grep -i bot | sort | uniq -c | sort -gr 
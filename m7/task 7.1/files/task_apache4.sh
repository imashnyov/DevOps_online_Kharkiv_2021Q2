#!/bin/bash
awk '
{
    if ($9 !~ /2../) print $7, $9
}' $1 | sort | uniq -c | sort -gr
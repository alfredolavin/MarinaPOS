#! /bin/sh
xclip -o | jq --compact-output --raw-output ' [.. | .name? | select(.)] | @csv'
